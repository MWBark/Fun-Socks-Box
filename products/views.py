from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, ProductImage
from .forms import ProductForm, ImageForm


def products(request):
    """Showns all products"""

    products = Product.objects.all()
    images = ProductImage.objects.all()
    cover_images = []

    for p in products:
        for i in images:
            if i.product == p:
                cover_images.append(i)
                break

    return render(
        request,
        'products/products.html',
        {
            'products': products,
            'cover_images': cover_images
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

    return render(request, 'products/product-detail.html', context)


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

    template = 'products/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    """Update a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Failed to add product. Please ensure the form is valid.")
    else:
        form = ProductForm(instance=product)

    template = 'products/update-product.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    messages.success(request, "Successfully deleted product!")
    return redirect(reverse('products'))


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
    """Add an image related to a product"""
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
    """Delete an image related to a product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    image = get_object_or_404(ProductImage, pk=image_id)
    image.delete()
    messages.success(request, "Successfully deleted image!")
    return redirect(reverse('images', args=[product_id]))

