from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Category(models.Model): 
    name = models.CharField(max_length=64) 
  
    @staticmethod
    def get_all_categories(): 
        return Category.objects.all() 
  
    def __str__(self): 
        return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    price = models.FloatField(default=0.0, validators=[MinValueValidator(0)])
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    
    def __str__(self): 
        return self.name 
    
    def get_absolute_url(self):
        return reverse("catalog-product", kwargs={"slug": self.slug})
    
