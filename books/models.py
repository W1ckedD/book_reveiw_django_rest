from django.db import models
from authors.models import Author

class Genre(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
    return self.title


class Book(models.Model):
  genres = models.ManyToManyField(Genre)
  title = models.CharField(max_length=150)
  description = models.TextField(blank=True)
  pages = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.title