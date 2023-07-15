from django.db import models
from django.contrib.auth.models import User


# Извиняюсь, что модели в одном месте_)
# Я обычно вот такие комменты не добавляю 😌

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    parent_category_id = models.BigIntegerField(null=True, blank=True, verbose_name="Если null, то это родитель")
    user_create = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    price = models.BigIntegerField()
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    user_create = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()
