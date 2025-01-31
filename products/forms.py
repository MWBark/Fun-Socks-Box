from django import forms
from .models import Product, ProductImage
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    Form class for adding products.
    """
    class Meta:
        model = Product
        fields = ('__all__')


class ImageForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = ('image',)

        image = forms.ImageField(
            label='Image', widget=CustomClearableFileInput
        )
