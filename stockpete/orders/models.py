from django.db import models
from stocks.models import Stock
from persons.models import Customer, Employee


# Create your models here.
class Order(models.Model):
    TYPES = [
        ("BUY", "BUY"),
        ("SELL", "SELL")
    ]
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPES)
    num = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stock)+" : "+str(self.type)+" : "+str(self.customer)