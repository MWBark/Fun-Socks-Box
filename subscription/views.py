from django.shortcuts import render

from products.models import ProductImage


def subscribe(request):
    """ A view to return subscription page """

    images = ProductImage.objects.all()

    return render(request, 'subscription/subscribe.html', {'images': images})
