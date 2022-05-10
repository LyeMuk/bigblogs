from django.db import models

# Create your models here.

"""category:
1:mental health
2:heart disease
3:covid
4:immunization"""
class Post(models.Model):
    img=models.ImageField(upload_to='myimage')
    sno=models.AutoField(primary_key=True)
    categoryid=models.CharField(max_length=10)
    author=models.CharField(max_length=20)
    uploaded = models.BooleanField()
    slug = models.CharField(max_length=100)
    title=models.CharField(max_length=255)
    summary=models.TextField()
    content=models.TextField()

class Userdb(models.Model):
    sno=models.AutoField(primary_key=True)
    email=models.CharField(max_length=255)
    uname=models.CharField(max_length=255)
    isdoctor = models.BooleanField()
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)