from django.urls import path

from apps.products.views import ProductCreateAPIView

app_name = 'products'

urlpatterns = [
    path('products/',ProductCreateAPIView.as_view())
]