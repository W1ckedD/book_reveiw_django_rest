from django.db import models
from users.models import User
from books.models import Book

class Rating(models.Model):
  value = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
  book = models.OneToOneField(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user + self.book + self.value