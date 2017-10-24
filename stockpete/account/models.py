from django.db import models
from persons.models import Customer
from stocks.models import Stock


# Create your models here.
class Account(models.Model):
    create_date = models.DateField(auto_created=True)
    customer = models.ForeignKey(Customer)
    password_hash = models.CharField(max_length=1000)
    card_no = models.CharField(max_length=16)

    def __str__(self):
        return str(self.customer)


class Portfolio(models.Model):
    account = models.ForeignKey(Account)
    stock = models.ForeignKey(Stock)
    num = models.PositiveIntegerField()

    def __str__(self):
        string = str(self.account)+" : "+str(self.stock)+" : "+str(self.num)
        return string
