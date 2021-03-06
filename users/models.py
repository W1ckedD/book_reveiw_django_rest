from django.db import models
from books.models import Book
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
  user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, related_name='profile')
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.first_name}, {self.middle_name[0].upper()}. {self.last_name}'


class CurrentlyReading(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  progress = models.IntegerField(default=0)

  def __str__(self):
    return self.user
