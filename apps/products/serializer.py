from django.utils.text import slugify
from rest_framework import serializers

from apps.products.id_generator import generate_id
from apps.products.models import Product, Category, Brand


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'slug': {'read_only': True},
            'is_active': {'read_only': True},
        }

    def create(self, validated_data):
        slug_base = slugify(validated_data.get('name'))
        slug = slug_base

        while Product.objects.filter(slug=slug).exists():
            slug = f"{slug_base}-{generate_id()}"
        validated_data['slug'] = slug
        return Product.objects.create(**validated_data)

    @staticmethod
    def validate_name(value):
        if not value:
            raise serializers.ValidationError("Name length must be greater than")
        return value

    @staticmethod
    def validate_price(value):
        if value < 0:
            raise serializers.ValidationError("Let the price be greater than 0")
        return value

    @staticmethod
    def validate_stock_quantity(value):
        if value < 0:
            raise serializers.ValidationError("The number of products must not be less than 0")
        return value

    @staticmethod
    def validate_discount_percentage(value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Discount percentage should be between 0 and 100")
        return value

    @staticmethod
    def validate_category(value):
        category = Category.objects.filter(id=value.id).exists()
        if not category:
            raise serializers.ValidationError("No such category exists")
        return value

    @staticmethod
    def validate_brand(value):
        brand = Brand.objects.filter(id=value.id).exists()
        if not brand:
            raise serializers.ValidationError("No such brand exists")
        return value


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock_quantity', 'discount_percentage']

    @staticmethod
    def validate_name(value):
        if not value:
            raise serializers.ValidationError("Name must not be empty")
        return value

    @staticmethod
    def validate_price(value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value

    @staticmethod
    def validate_stock_quantity(value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity must be >= 0")
        return value

    @staticmethod
    def validate_discount_percentage(value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Discount percentage must be between 0 and 100")
        return value


    def update(self, instance, validated_data):
        if 'name' in validated_data:
            slug_base = slugify(validated_data['name'])
            slug = slug_base
            while Product.objects.filter(slug=slug).exclude(id=instance.id).exists():
                slug = f"{slug_base}-{generate_id()}"
            instance.slug = slug

        return super().update(instance, validated_data)



class ProductPartialUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock_quantity', 'discount_percentage']

    @staticmethod
    def validate_name(value):
        if not value:
            raise serializers.ValidationError("Name must not be empty")
        return value

    @staticmethod
    def validate_price(value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value

    @staticmethod
    def validate_stock_quantity(value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity must be >= 0")
        return value

    @staticmethod
    def validate_discount_percentage(value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Discount percentage must be between 0 and 100")
        return value

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            slug_base = slugify(validated_data['name'])
            slug = slug_base
            while Product.objects.filter(slug=slug).exclude(id=instance.id).exists():
                slug = f"{slug_base}-{generate_id()}"
            instance.slug = slug
        return super().update(instance, validated_data)

