from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.utils.datetime_safe import datetime

from main.forms import AddTransactionForm
from main.models import TransactionType, Transaction


class ChartData:
    def __init__(self, labels, data):
        self.labels = labels
        self.data = data


@login_required
def index(request):
    return render(request, 'main/main.html')


@login_required
def transactions(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            print(obj)
    form = AddTransactionForm()
    trantypes = TransactionType.objects.filter(Q(user=None) | Q(user=request.user))
    transactions = Transaction.objects.filter(user=request.user)

    return render(request, 'main/transactions.html',
                  {'form': form, 'transaction_types': trantypes, 'transactions': transactions,
                   'chartCircle': circle_data(), 'chartMonth': month_transactions()})


def circle_data():
    trans_types = {}
    type_translate = {}
    for typ in TransactionType.objects.filter(user__isnull=True):
        type_translate[typ.id] = typ.name
        trans = Transaction.objects.filter(type=typ, datetime__month=datetime.today().month).all()
        for tran in trans:
            trans_types.setdefault(typ.id, 0)

            trans_types[typ.id] += tran.amount
    print(type_translate[1])
    data = {"labels": [type_translate[tran_id] for tran_id in trans_types.keys()],
            "data": list(trans_types.values())}
    return ChartData(data["labels"], data["data"])


def month_transactions():
    months = ["Январь",
              "Февраль",
              "Март",
              "Апрель",
              "Май",
              "Июнь",
              "Июль",
              "Авугст",
              "Сентябрь",
              "Октябрь",
              "Ноябрь",
              "Декабрь", ]
    tran_month = {}
    for i in range(3):
        dt = datetime.now() - timedelta(days=30 * i)
        for typ in TransactionType.objects.filter(user__isnull=True):
            trans = Transaction.objects.filter(type=typ, datetime__month=dt.month).all()
            for tran in trans:
                tran_month.setdefault(dt.month, 0)
                tran_month[dt.month] += tran.amount
    data = {"labels": [months[i] for i in tran_month.keys()],
            "data": list(tran_month.values())}

    return ChartData(data["labels"], data["data"])
