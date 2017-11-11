from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.0'))])
    num_avail_shares = models.PositiveIntegerField()
    stock_type = models.CharField(max_length=100)

    @property
    def cur_price(self):
        return self.price

    def __str__(self):
        return self.symbol
