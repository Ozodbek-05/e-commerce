from django.urls import path

from apps.orders.views import home_view

app_name = 'orders'

urlpatterns = [
    path('/',home_view,name='home')
]