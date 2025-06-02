from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Product, ProductImage, Category
from rest_framework.permissions import IsAuthenticated

class ProductCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user

        # Cria produto
        product = Product.objects.create(
            user=user,
            name=data.get('name'),
            sku=data.get('sku'),
            brand=data.get('brand'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            price=data.get('price'),
            discount_price=data.get('discount_price') or None,
            stock_quantity=data.get('stock_quantity'),
            is_available=data.get('is_available') == 'true',
            is_featured=data.get('is_featured') == 'true',
            shipping_info=data.get('shipping_info'),
            warranty_info=data.get('warranty_info'),
            meta_title=data.get('meta_title'),
            meta_description=data.get('meta_description'),
            meta_keywords=data.get('meta_keywords'),
        )

        # Múltiplas categorias (espera lista de IDs)
        category_ids = request.data.getlist('categories')
        product.categories.set(Category.objects.filter(id__in=category_ids))

        # Imagens
        for img in request.FILES.getlist('images'):
            ProductImage.objects.create(product=product, image=img)

        return Response({'message': 'Produto criado com sucesso'})
