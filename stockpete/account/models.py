from django.db import models
from persons.models import Customer
from stocks.models import Stock
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    card_no = models.CharField(max_length=16)
    card_exp = models.DateField(default="2040-01-01")

    def __str__(self):
        return str(self.customer)


class Portfolio(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(default=0)

    def __str__(self):
        string = str(self.account)+" : "+str(self.stock)+" : "+str(self.num)
        return string
