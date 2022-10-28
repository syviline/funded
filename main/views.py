from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from main.forms import AddTransactionForm
from main.models import TransactionType


@login_required
def index(request):
    return render(request, 'main/main.html')


@login_required
def transactions(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
    form = AddTransactionForm()
    trantypes = TransactionType.objects.filter(Q(user=None) | Q(user=request.user))
    return render(request, 'main/transactions.html', {'form': form, 'transaction_types': trantypes})