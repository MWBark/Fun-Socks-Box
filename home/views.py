from django.shortcuts import render


def index(request):
    """ Aview to return index page """
    return render(request, 'home/index.html')
