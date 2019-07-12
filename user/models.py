from django.db import models

# Create your models here.

class Home_user(models.Model):
    hid = models.IntegerField(primary_key=True,auto_created=True)
    account = models.CharField(max_length=20)
    hname = models.CharField(max_length=20)
    hpwd = models.CharField(max_length=150)
    tel = models.IntegerField()
    address = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    avatar = models.CharField(max_length=40,null=True)#存储头像所储存的地址

    class Meta:
        db_table = 'home_user'

class Courier_user(models.Model):
    cid = models.IntegerField(primary_key=True, auto_created=True)
    cname = models.CharField(max_length=20)
    cpwd = models.CharField(max_length=40)
    tel = models.IntegerField()
    email = models.CharField(max_length=40)

    class Meta:
        db_table = 'courier_user'

