from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kategori Adı")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name=models.CharField(max_length=100, verbose_name="Alt Kategori")
    def __str__(self):
        return self.name
    



class Product (models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Satıcı",null=True,editable=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,verbose_name="Kategori")
    sub_category = models.ManyToManyField(SubCategory, verbose_name=("Alt Kategori"))
    name=models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to="products", null=True,blank=True) #blank zorunluluğu kaldırır.
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi",null=True)

    def __str__(self):
        return self.name #admin panelindeki görünecek kısmı ayarlıyoruz. 