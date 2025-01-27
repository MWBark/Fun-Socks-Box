from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Address
from .forms import AddressForm


@login_required
def addresses(request):
    """"""
    profile = get_object_or_404(Profile, user=request.user)
    addresses = Address.objects.filter(user=profile)

    template = 'profiles/addresses.html'
    context = {
        'addresses': addresses,
    }

    return render(request, template, context)


@login_required
def add_address(request):
    """Add an address."""
    profile = get_object_or_404(Profile, user=request.user)
    addresses = Address.objects.filter(user=profile)

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = profile
            form.save()

            messages.success(request, "Address added successfully")
            return redirect(reverse('addresses'))
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = AddressForm()
    
    template = 'profiles/add-address.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_address(request, address_id):
    """Update an address."""
    profile = get_object_or_404(Profile, user=request.user)
    addresses = Address.objects.filter(user=profile)
    address = get_object_or_404(Address, pk=address_id)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()

            messages.success(request, "Address updated successfully")
            return redirect(reverse('addresses'))
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = AddressForm(instance=address)

    template = 'profiles/update-address.html'
    context = {
        'form': form,
        'address': address,
    }

    return render(request, template, context)


@login_required
def delete_address(request, address_id):
    """Delete an address."""
    address = get_object_or_404(Address, pk=address_id)
    address.delete()

    messages.success(request, "Address deleted successfully")
    return redirect(reverse('addresses'))


@login_required
def set_default(request, address_id):
    """Set an address as default."""
    profile = get_object_or_404(Profile, user=request.user)
    addresses = Address.objects.filter(user=profile)
    address = get_object_or_404(Address, pk=address_id)

    for a in addresses:                    
        a.default = False
        a.save()

    address.default = True
    address.save()

    messages.success(request, "Default set successfully")
    return redirect(reverse('addresses'))
