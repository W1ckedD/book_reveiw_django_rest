from django.db import models

from users.models import User
from books.models import Book

class Review(models.Model):
  content = models.TextField(blank=True)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user + self.book