from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import MessageForm


def contact(request):
    """"""
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save()
            messages.success(request, "Message sent!")
            return redirect(reverse('contact'))
        else:
            messages.error(request, "Failed to send message. Please ensure the form is valid.")

    if request.user.is_authenticated:
        form = MessageForm(initial={
            'email': request.user.email
        })
    else:
        form = MessageForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
