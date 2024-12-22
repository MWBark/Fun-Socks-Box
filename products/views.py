from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, ProductImage
from .forms import ProductForm, ImageForm


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


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to add product. Please ensure the form is valid.")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def images(request, product_id):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product=product)
    form = ImageForm()

    template = 'products/images.html'
    context = {
        'product': product,
        'images': images,
        'form': form,
    }

    return render(request, template, context)


def add_image(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            product_image = form.save(commit=False)
            product_image.product = product
            product_image.save()
            messages.success(request, "Successfully added image!")
            return redirect(reverse('images', args=[product_id]))
        else:
            messages.error(request, "Failed to add image. Please ensure the form is valid.")


def delete_image(request, product_id, image_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    image = get_object_or_404(ProductImage, pk=image_id)
    image.delete()
    messages.success(request, "Successfully deleted image!")
    return redirect(reverse('images', args=[product_id]))

