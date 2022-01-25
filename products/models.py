from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Product representation
    """
    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")
    price = models.DecimalField("Price", validators=[MinValueValidator(0.01)])
    image = models.ImageField("Image", upload_to="products")

    def __str__(self):
        return self.name