from django.contrib import admin
from .models import Address

class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'street_address1',
    )


admin.site.register(Address, AddressesAdmin)
