from django.db import models

class Product(models.Model):

    upc = models.PositiveIntegerField(null=False, unique=True, default=None)
    main_image = models.URLField(blank=True, null=True, default=None)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    brand = models.CharField(max_length=128, blank=True, null=True, default=None)
    model_product = models.CharField(max_length=128, blank=True, null=True, default=None)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    in_stock = models.BooleanField()
    price = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    free_shipping = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)
