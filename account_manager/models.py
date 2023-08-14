from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from complain.models import Nature

# Create your models here.
# class Role(models.Model):
#     id_role=models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)


class Account_manager(models.Model):
    id_manager=models.AutoField(primary_key=True)
    lastname=models.CharField(max_length=20)
    firstname=models.CharField(max_length=100)
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=10)
    phone_number = PhoneNumberField(blank=True)
    role=models.ForeignKey(Nature,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.username} - {self.firstname} {self.lastname}" 

