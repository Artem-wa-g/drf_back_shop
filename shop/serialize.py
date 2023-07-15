from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    # user =
    class Meta:
        model = Product
        fields = (
            "name",
            "subgroup",
            "price",
            "deleted",
            "idCategory",
            "description",
        )
        # fields = ("__all__")  # Если хотим вернуть все поля

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

