from rest_framework import generics
from rest_framework import response
from rest_framework.response import Response
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

class BookList(generics.ListAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()


class RetrieveBook(generics.RetrieveAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  lookup_field='id'

class BooksByGenre(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  def list(self, request, *args, **kwargs):
    queryset = Book.objects.filter(genres=kwargs['genre_id'])
    serializer = self.get_serializer(queryset, many=True)
    return Response({
      'books': serializer.data
    })