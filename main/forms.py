from django import forms

from main.models import Transaction


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'name', 'amount']

