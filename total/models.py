from django.db import models

# Create your models here.
class client(models.Model):
    id = models.AutoField
    date = models.DateField()
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    mail = models.EmailField()
    location = models.CharField(max_length=100)
    domain = models.CharField(max_length=100, null=True)
    domainname = models.CharField(max_length=100, null=True)
    domainpurchase = models.DateField(null=True)
    domainexpiry = models.DateField(null=True)
    host = models.CharField(max_length=100, null=True)
    hostpurchase = models.DateField(null=True)
    hostexpiry = models.DateField(null=True)
    emailtype = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, )
    emailcompany = models.CharField(max_length=100, null=True)
    emailpurchase = models.DateField(null=True)   
    emailexpiry = models.DateField(null=True)
    
