from rest_framework import serializers
from .models import Book, Category, Collection


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CollectionSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(many=True)

    class Meta:
        model = Collection
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
