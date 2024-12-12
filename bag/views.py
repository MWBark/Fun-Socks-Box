from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, ProductImage


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    product_images = ProductImage.objects.filter(product=product)
    product_image = product_images[0]
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(request, f'Added size {size.upper()} {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)