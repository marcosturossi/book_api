from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Book, Category, Collection
from .serializers import BookSerializer, CategorySerializer, CollectionSerializer


class ApiRoot(generics.GenericAPIView):
    name = 'api_root'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({'categories': reverse(CategoryListCreateView.name, request=request),
                         'books': reverse(BookListCreateView.name, request=request),
                         #'collections': reverse(CollectionRetrieveView.name,request=request)
        })


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'collections:book_list'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'collections:book_detail'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'collections:category_list'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'collections:category_detail'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


class CollectionRetrieveView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    name = 'collections:collection_detail'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
