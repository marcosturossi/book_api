from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import Book, Category, Collection
from .serializers import BookSerializer, CategorySerializer, CollectionSerializer


class Documentation(TemplateView):
    template_name = 'documentation.html'


class ApiRoot(generics.GenericAPIView):
    name = 'api_root'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({'categories': reverse(CategoryListCreateView.name, request=request),
                         'books': reverse(BookListCreateView.name, request=request),
                         'collections': reverse(CollectionRetrieveView.name,
                                                kwargs={'pk': self.request.user.collection.id}, request=request)})


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'collections:book_list'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filterset_fields = ['category', 'author']

    def get_queryset(self):
        # Aplica o filtro para exibir apenas os livros do Usuário
        return Book.objects.filter(category__collection__user=self.request.user.id)


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'collections:book_detail'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        if obj.category.collection.user != self.request.user:
            raise PermissionDenied({'message': "You don't have permission to acess"})
        return obj


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'collections:category_list'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    filterset_fields = ['name']

    def get_queryset(self):
        # Aplica o filtro para exibir apenas as Categorias do Usuário
        return Category.objects.filter(collection__user=self.request.user.id)


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'collections:category_detail'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        if obj.collection.user != self.request.user:
            raise PermissionDenied({'message': "You don't have permission to acess"})
        return obj


class CollectionRetrieveView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    name = 'collections:collection_detail'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        if obj.user != self.request.user:
            raise PermissionDenied({'message': "You don't have permission to acess"})
        return obj
