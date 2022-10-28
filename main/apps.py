from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from main.models import TransactionType

        default_transaction_types = ['Продукты', 'Шоппинг', 'Транспорт', 'Здоровье', 'Одежда']

        objs = TransactionType.objects.filter(user=None).values('name')
        names = []
        for i in objs:
            names.append(i['name'])
        for i in default_transaction_types:
            # TransactionType(name=i).save()
            if i not in names:
                TransactionType(name=i).save()