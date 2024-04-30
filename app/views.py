from rest_framework import generics
from .models import Book
from .serializer import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.select_related('author').prefetch_related('genres').all()
    serializer_class = BookSerializer
