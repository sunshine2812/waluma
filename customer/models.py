from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    account_number = models.IntegerField(primary_key=True, unique=True)
    customer_style = (("P","physique"),("M","morale"))
    style=models.CharField(choices=customer_style,max_length=1)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=10)
    phone_number = PhoneNumberField(blank=True)
    lastname=models.CharField(max_length=20)
    firstname=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.account_number} - {self.style}-{self.email}-{self.username} - {self.password} - {self.phone_number}"