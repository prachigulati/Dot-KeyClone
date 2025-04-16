from django.contrib import admin
from . models import Category , Product
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)