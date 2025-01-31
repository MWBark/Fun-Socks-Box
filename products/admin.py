from django.contrib import admin
from .models import Product, ProductImage


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )

    ordering = ('name',)


admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductImage)
