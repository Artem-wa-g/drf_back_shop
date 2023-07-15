from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    # Чтобы автоматом в создателя подставлялся пользователь, как создатель
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"  # Если хотим вернуть все поля
        # fields = (  # Можно указывать конкретные поля
        #     'name',
        #     'price',
        #     'category_id',
        #     'description',
        #     'user_create_id',
        #     'date_create',
        #     'date_update',
        #     'deleted',
        # )

        # TODO: имеет смысл, но не удобно. Наследоваться должны от serializers.Serializer
        # name = serializers.CharField(max_length=128)
        # subgroup = serializers.CharField(max_length=128)
        # price = serializers.IntegerField
        # deleted = serializers.BooleanField(read_only=True)
        # idCategory = serializers.IntegerField(read_only=True)
        # description = serializers.CharField(max_length=1024, read_only=True)
        #
        # def create(self, validated_data):
        #     return Product.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.subgroup = validated_data.get('subgroup', instance.subgroup)
        #     instance.price = validated_data.get('price', instance.price)
        #     instance.deleted = validated_data.get('deleted', instance.deleted)
        #     instance.idCategory = validated_data.get('idCategory', instance.idCategory)
        #     instance.description = validated_data.get('description', instance.description)
        #     instance.save()
        #     return instance


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"

