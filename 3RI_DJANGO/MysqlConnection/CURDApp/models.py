from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    ename = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    econtact = models.CharField(max_length=10)

    class Meta:
        db_table = "employee"

# class Users(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#
#     class Meta:
#         db_table = "Users"
