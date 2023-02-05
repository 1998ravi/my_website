from django.core import exceptions
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.db.models.fields.files import ImageField

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    @staticmethod
    def get_cust_email(email):
        try:
            return User.objects.get(email=email)
        except:
            print("error happend")

class cat(models.Model):
    category=models.CharField(max_length=100,default="books")
    def __str__(self) -> str:
        return self.category
class post(models.Model):
    title=models.CharField(max_length=50)
    post=models.TextField()
    Image=models.ImageField(upload_to='image/')
    cate=models.ForeignKey(cat,on_delete=CASCADE,null=True)
    user=models.CharField(max_length=100,default="from website")
    email=EmailField(default="rk0901308@gmail.com")
    def __str__(self) -> str:
         return self.title
class Comments(models.Model):
    post=models.ForeignKey('post',on_delete=models.CASCADE)
    commets=models.TextField()
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.commets

class enq(models.Model):
    emailenq=models.EmailField()
    ques=models.TextField()
    def __str__(self) -> str:
        return self.ques



class dem(models.Model):
    img=models.ImageField(upload_to='demo/')