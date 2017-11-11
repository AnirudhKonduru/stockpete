from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    ph_num = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.DecimalField(decimal_places=0, max_digits=6)

    def __str__(self):
        return str(self.pk)+" - "+self.first_name+" "+self.last_name

    class Meta:
        abstract = True


class Customer(Person):
    email = models.CharField(max_length=50)
    rating = models.DecimalField(decimal_places=2, max_digits=4, default=10)


class Employee(Person):
    ssn = models.CharField(max_length=20)
    start_date = models.DateField(auto_created=True)
    hourly_rate = models.DecimalField(decimal_places=2, max_digits=4)
