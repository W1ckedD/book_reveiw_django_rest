from django.db import models
from books.models import Book
from users.models import User

class Shelf(models.Model):
  name = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  books = models.ManyToManyField(Book)