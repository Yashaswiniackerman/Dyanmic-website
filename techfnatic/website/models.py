from django.db import models

# Create your models here.
class SocialLinks(models.Model):
    linkedin = models.CharField(max_length=150)
    facebook = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.phoneno
    
class Info(models.Model):
    webimage = models.ImageField(upload_to='website/images', default ="")
    weblogo = models.ImageField(upload_to='website/images',default ="")
    webintro = models.TextField(max_length=1000,default ="")
    aboutus = models.TextField(max_length=1000, default ="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self) -> str:
      return self.webintro
    
class Location(models.Model):
    address = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.address
    
class Product(models.Model):
    productimage = models.ImageField(upload_to='website/images')
    productname = models.CharField(max_length=26)
    description = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return self.productname
