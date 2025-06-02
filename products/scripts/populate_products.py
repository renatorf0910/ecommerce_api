import random
from django.utils.text import slugify
from django.utils import timezone
from products.models import Product
from django.contrib.auth.models import User

brands = ['Nike', 'Adidas', 'Vans', 'Puma', 'Asics', 'Fila', 'Reebok']
short_descriptions = [
    'Calçado esportivo confortável.',
    'Ideal para corridas e caminhadas.',
    'Design moderno e leve.',
    'Estilo e performance para o dia a dia.',
    'Tecnologia de amortecimento avançada.',
]

descriptions = [
    'Produto ideal para quem busca desempenho e estilo. Confortável para o uso diário.',
    'Feito com materiais de alta qualidade. Leve e resistente.',
    'Tênis com acabamento premium e visual moderno. Testado por atletas.',
    'Experimente um novo patamar de conforto. Indicado para todos os terrenos.',
    'Tecnologia exclusiva que proporciona maior estabilidade em suas atividades.',
]

for i in range(1, 121):
    name = f"TÊNIS MODELO {i}"
    slug = slugify(name)
    sku = f"SKU{i:05d}"
    brand = random.choice(brands)
    short_description = random.choice(short_descriptions)
    description = random.choice(descriptions)
    price = round(random.uniform(100, 500), 2)
    discount_price = round(price * random.uniform(0.5, 0.9), 2)
    stock_quantity = random.randint(10, 200)
    is_available = True
    is_featured = random.choice([True, False])
    specs = ''
    rating = 0.0
    num_reviews = 0
    shipping_info = ''
    warranty_info = ''
    meta_title = ''
    meta_description = ''
    meta_keywords = ''
    created_at = timezone.now()
    updated_at = timezone.now()
    user_id = random.randint(1, 16)

    Product.objects.create(
        name=name,
        slug=slug,
        sku=sku,
        brand=brand,
        short_description=short_description,
        description=description,
        price=price,
        discount_price=discount_price,
        stock_quantity=stock_quantity,
        is_available=is_available,
        is_featured=is_featured,
        specs=specs,
        rating=rating,
        num_reviews=num_reviews,
        shipping_info=shipping_info,
        warranty_info=warranty_info,
        meta_title=meta_title,
        meta_description=meta_description,
        meta_keywords=meta_keywords,
        created_at=created_at,
        updated_at=updated_at,
        user_id=user_id,
    )

print("✅ Inserção de produtos concluída com sucesso.")
