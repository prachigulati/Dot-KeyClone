from django.db import models

# Create your models here.


#Categories of product
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



#Products
class Product(models.Model):
    name =  models.CharField(max_length=100)
    price =  models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description =  models.CharField(max_length=250,default=' ',blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    tag=models.CharField(max_length=50)
    # type=models.CharField(max_length=50)
    rating=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    rating_next=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    weight=models.CharField(max_length=50)
    #add sale
    is_sale = models.BooleanField(default=False)
    sale_percentage = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    def __str__(self):
        return self.name
