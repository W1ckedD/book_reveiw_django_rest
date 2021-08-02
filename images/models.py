from django.db import models
from authors.models import Author
from books.models import Book
from users.models import User

class Photo(models.Model):
  image = models.ImageField(upload_to='photos/%Y/%m/%d/')
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='images')
  author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE, related_name='images')
  book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE, related_name='images')

  def __str__(self):
    return self.image.url
