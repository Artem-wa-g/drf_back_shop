from django.contrib import admin

from .models import Product, Category, Role, UserToRole, User

# Register your models here.
admin.site.register(Product)
