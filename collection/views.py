from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()  # TODO refatorar para filtar query por usuário
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    pass
