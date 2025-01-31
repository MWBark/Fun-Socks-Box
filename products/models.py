from django.db import models


class Product(models.Model):
    """Contains product info"""
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    """Contains image related to specific product"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
