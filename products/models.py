from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Product representation
    """
    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")
    price = models.DecimalField(
        "Price", 
        decimal_places=2, 
        max_digits=9, 
        validators=[MinValueValidator(0.01)]
    )
    image = models.ImageField("Image", upload_to="products")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']