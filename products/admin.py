from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
