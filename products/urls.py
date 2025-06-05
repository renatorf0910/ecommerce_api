from django.urls import path
from .views import ProductCreateView, ProductViewSet, OwnerProductViewSet, ProductDetailAPIView

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='products'),
    path('products/myproducts/', OwnerProductViewSet.as_view({'get': 'list'}), name='myproducts'),
    path('products/product/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
