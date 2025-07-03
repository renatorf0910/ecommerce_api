from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product

class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'slug']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductInCartSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, source="product"
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quatity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
        read_only_fields = ['user']