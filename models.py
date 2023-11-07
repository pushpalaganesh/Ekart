from django.db import models

class students_data(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    course=models.CharField(max_length=40)
    fee=models.BigIntegerField()
    assignment1=models.BigIntegerField()
    assignment2=models.BigIntegerField()
    assignment3=models.BigIntegerField()
    assignment4=models.BigIntegerField()
    institute=models.CharField(max_length=40)
    location=models.CharField(max_length=40)