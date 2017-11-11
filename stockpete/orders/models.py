from django.db import models
from stocks.models import Stock
from persons.models import Customer, Employee
from account.models import Account


# Create your models here.
class Order(models.Model):
    TYPES = [
        ("BUY", "buy"),
        ("SELL", "sell")
    ]
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPES)
    num = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=None, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return str(self.stock)+" : "+str(self.type)+" : "+str(self.customer)
