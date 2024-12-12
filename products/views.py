from django.shortcuts import render, get_object_or_404

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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'images': images,
    }

    return render(request, 'products/product_detail.html', context)