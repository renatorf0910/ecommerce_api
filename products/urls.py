from django.urls import path
from .views import ProductCreateView

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
]
