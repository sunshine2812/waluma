from django.db import models
from customer.models import Customer



# Create your models here.

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Nature(models.Model):
    id_nature = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Complain(models.Model):
      
    id_complain = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=2000,blank=True)
    attached_file = models.ImageField(upload_to="uploads/", null=True, blank=True)
    account_number = models.ForeignKey(Customer,on_delete=models.CASCADE)
    id_nature = models.ForeignKey(Nature,on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status,on_delete=models.CASCADE)
    