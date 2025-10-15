from django.urls import path

from apps.reviews.views import home_view

app_name = 'reviews'

urlpatterns = [
    path('/',home_view,name='home')
]