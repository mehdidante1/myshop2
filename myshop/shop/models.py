from typing import Reversible
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.conf.urls.static import static
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
 
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
   

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id , self.slug])
    
    

    class Meta:
        ordering = ("name",)
        index_together = (('id', 'slug',))
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class Product_mobile(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="productss")
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    description_2 = models.TextField(blank=True)
    description_3 = models.TextField(blank=True)
    description_4 = models.TextField(blank=True)
    internal_memory =models.CharField(max_length=200, db_index=True)
    internal_network =models.CharField(max_length=200, db_index=True)
    photo_resolution =models.CharField(max_length=200, db_index=True)
    number_simcard= models.CharField(max_length=200, db_index=True)
    special_features = models.CharField(max_length=200, db_index=True)
    dimensions = models.CharField(max_length=200, db_index=True)
    description_simcard = models.CharField(max_length=200, db_index=True)
    chipset = models.CharField(max_length=200, db_index=True)
    type_Processor= models.CharField(max_length=200, db_index=True) 
    price = models.CharField(max_length=70)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id , self.slug])



    class Meta:
        ordering = ("name",)
        index_together = (('id', 'slug',))
        verbose_name_plural = "Products_mobiles"

    def __str__(self):
        return self.name


class Comments (models.Model):
    product = models.ForeignKey("Product" , verbose_name=_("محصول") , related_name="comments" , on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"),max_length=100)
    email = models.EmailField(_("آدرس الکترونیکی"),max_length=200)
    massage = models.TextField(_("متن نظر"))
    available = models.BooleanField(default=False)
    date = models.DateTimeField(_("تاریخ انتشار"), auto_now=True , auto_now_add=False)



      
