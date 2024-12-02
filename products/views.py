from django.shortcuts import render

from .models import Product, ProductImage


def products(request):

    products = Product.objects.all()
    images = ProductImage.objects.all()

    return render(
        request,
        'products/products.html',
        {
            'products': products,
            'images': images
        }
    )
