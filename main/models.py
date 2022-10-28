from django.contrib.auth import get_user_model
from django.db import models


class TransactionType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, verbose_name='Тип')
    name = models.CharField('Название', max_length=255)
    amount = models.FloatField('Сумма')
    datetime = models.DateTimeField(auto_now_add=True)