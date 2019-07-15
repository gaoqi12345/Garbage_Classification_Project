from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30,verbose_name='用户名')
    nickname = models.CharField(max_length=30,verbose_name='昵称')
    password = models.CharField(max_length=150,verbose_name='密码')
    tel = models.CharField(max_length=20,verbose_name='电话号码')
    address = models.CharField(max_length=150,verbose_name='地址')
    email = models.EmailField(max_length=60,verbose_name='邮箱')
    category=models.CharField(max_length=30,verbose_name='用户类别')
    avatar = models.ImageField(max_length=200,null=True,upload_to='avatar/',verbose_name='头像')#存储头像所储存的地址

    class Meta:
        db_table = 'user'

    def __str__(self):
        return "用户 " + self.username



