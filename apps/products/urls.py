from django.urls import path
from apps.products.views import (
    ProductCreateAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView
)

app_name = 'products'

urlpatterns = [
    path('products/', ProductCreateAPIView.as_view(), name='create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='detail'),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='update'),
    path('products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='delete'),
]
