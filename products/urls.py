from django.urls import path
from .views import FavoriteViewSet, ProductCreateView, ProductViewSet, OwnerProductViewSet, ProductDetailAPIView, ProductImageAPIView

favorite_list = FavoriteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

favorite_detail = FavoriteViewSet.as_view({
    'delete': 'destroy',
})

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='products'),
    path('products/myproducts/', OwnerProductViewSet.as_view({'get': 'list'}), name='myproducts'),
    path('products/product/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/product_image/<int:id>/', ProductImageAPIView.as_view(), name='product-image-detail'),
    path('favorites/', favorite_list, name='favorite-list'),
    path('favorites/<int:pk>/', favorite_detail, name='favorite-detail'),
]
