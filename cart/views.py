from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer
from django.shortcuts import get_object_or_404

class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        if not product_id:
            return Response(
                {"error": "O campo 'product_id' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            quantity = int(request.data.get("quantity", 1))
        except ValueError:
            return Response(
                {"error": "O campo 'quantity' deve ser um número inteiro."},
                status=status.HTTP_400_BAD_REQUEST
            )
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = CartItemSerializer(data={
            "product_id": product_id,
            "quantity": quantity,
        })
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item = get_object_or_404(CartItem, cart=cart, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)