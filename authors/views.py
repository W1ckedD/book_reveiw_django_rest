from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer



class AuthorsAPIView(ListAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class AuthorAPIView(RetrieveAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  lookup_field = 'id'

class AuthorBookAPIView(GenericAPIView):
  serializer_class = BookSerializer
  queryset = Book.objects.all()
  lookup_field = 'id'
  def get(self, request, *args, **kwargs):
    queryset = Book.objects.filter(author=kwargs['id'])
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)