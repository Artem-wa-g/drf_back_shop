from django.db import models


# Извиняюсь, что модели в одном месте_)
# ну и для названия товара и подгруппы лучше, наверное, использовать enum

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True, blank=True)
    login = models.CharField(max_length=128, unique=True)
    passwordHash = models.CharField(max_length=512, blank=True)
    deleted = models.BooleanField


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    deleted = models.BooleanField()


class UserToRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    idUser = models.ForeignKey(to=User, on_delete=models.CASCADE)
    idRole = models.ForeignKey(to=Role, on_delete=models.CASCADE)
    date_joined = models.DateField()


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    # idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    idUserCreate = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    deleted = models.BooleanField


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    subgroup = models.CharField(max_length=128)
    price = models.BigIntegerField()
    deleted = models.BooleanField()
    idCategory = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
