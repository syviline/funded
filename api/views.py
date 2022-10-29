from django.shortcuts import render
from django.http import JsonResponse, response

# Create your views here.
from django.utils.datetime_safe import datetime
from datetime import timedelta

from main.models import Transaction, TransactionType


def circle(request):
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
    return JsonResponse(data)


def monthе_transactions(request):
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
    return JsonResponse(data)
