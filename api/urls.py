from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path('api/circle', views.circle, name='api_get_circle'),
    path('api/monthTransactions', views.monthе_transactions, name='api_get_month_transactions'),
]
