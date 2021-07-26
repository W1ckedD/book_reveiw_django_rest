from django.db import models
from authors.models import Author

class Website(models.Model):
  name = models.CharField(max_length=255)
  url = models.CharField(max_length=255)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  def __str__(self):
    return self.name