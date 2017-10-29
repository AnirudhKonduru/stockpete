from django.db import models
from persons.models import Customer
from stocks.models import Stock


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20)
    create_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    card_no = models.CharField(max_length=16)
    card_exp = models.DateField(default="2040-01-01")

    def __str__(self):
        return str(self.customer)


class Portfolio(models.Model):
    account = models.ForeignKey(Account)
    stock = models.ForeignKey(Stock)
    num = models.PositiveIntegerField()

    def __str__(self):
        string = str(self.account)+" : "+str(self.stock)+" : "+str(self.num)
        return string
