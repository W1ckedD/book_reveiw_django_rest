from authors.serializers import AuthorSerializer
from rest_framework import serializers
from .models import Book, Genre
from authors.models import Author

class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('title',)

class BookSerializer(serializers.ModelSerializer):
  genres = serializers.StringRelatedField(many=True, read_only=True)
  class Meta:
    model = Book
    fields = '__all__'