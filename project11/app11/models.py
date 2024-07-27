from django.db import models
from django.contrib.auth.models import User


class RegistrationForm(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=25)
    cpassword=models.CharField(max_length=25)
class LoginForm(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=25)

    

class Product(models.Model):
    pname=models.CharField(max_length=50)
    pcost=models.FloatField()
    cat=models.IntegerField()
    pdetails=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')
    def __str__(self):
        return self.pname
    
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

