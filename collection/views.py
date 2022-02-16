from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response

from .models import Book, Category, Collection
from .serializers import BookSerializer, CategorySerializer, CollectionSerializer


class ApiRoot(generics.GenericAPIView):
    name = 'api_root'

    def get(self, request, *args, **kwargs):
        # TODO Implementar o reverse para a coleção do usuário
        return Response({'categories': reverse(CategoryListCreateView.name, request=request),
                         'books': reverse(BookListCreateView.name, request=request),
                         'collections': reverse(CollectionRetrieveView.name, request=request)})


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'collections:book_list'


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'collections:book_detail'


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'collections:category_list'


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'collections:category_detail'


class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    name = 'collections:collectio_add'


class CollectionRetrieveView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    name = 'collections:collection_detail'