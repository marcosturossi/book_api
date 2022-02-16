from rest_framework import serializers
from .models import Book, Category


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        dept = 2


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Category
        fields = "__all__"
