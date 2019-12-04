from django.db import models

# Create your models here.
class transaction_Details(models.Model):
    transaction_id = models.CharField(max_length=20,primary_key=True)
    paypal_reference_id = models.CharField(max_length=20)
    transactioon_initiation_date=models.DateTimeField()
    #transaction_amount
    currency_code=models.CharField(max_length=3)
    value=models.DecimalField(max_digits=50,decimal_places=4)


class shipping_info(models.Model):
    Transaction_id=models.CharField(max_length=20,primary_key=True)
    name =models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    line1= models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    country_code= models.CharField(max_length=3)
    postal_code= models.CharField(max_length=8)

