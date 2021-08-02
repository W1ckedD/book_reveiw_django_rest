from authors.serializers import AuthorSerializer
from rest_framework import serializers
from .models import Book, Genre
from authors.models import Author
from images.models import Photo
from images.serializers import PhotoSerializer

class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('title',)

class BookSerializer(serializers.ModelSerializer):
  images = PhotoSerializer(many=True)
  genres = serializers.StringRelatedField(many=True, read_only=True)
  author = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = Book
    fields = ('id', 'genres', 'title', 'author', 'images', 'description', 'pages')