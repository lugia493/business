from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Tenant(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    ownership = models.ImageField(null=True, blank=True) 
    video = models.ImageField(null=True, blank=True) 
    identity = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.user.name)

class Landlord(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    credit = models.ImageField(null=True, blank=True) 
    employment = models.ImageField(null=True, blank=True) 
    identity = models.ImageField(null=True, blank=True) 
    
    def __str__(self):
        return str(self.user.name)

class Order(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    complete_tenant = models.BooleanField(null=True, default=False)
    complete_landlord = models.BooleanField(null=True, default=False)
    transaction_id = models.CharField(max_length=100, null=True)
   
    def __str__(self):
        return str(self.id)