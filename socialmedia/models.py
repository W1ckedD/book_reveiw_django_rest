from django.db import models
from users.models import User
from authors.models import Author

class SocialMediaType(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class SocialMedia(models.Model):
  url = models.CharField(max_length=255)
  type = models.ForeignKey(SocialMediaType, on_delete=models.DO_NOTHING)
  author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
  user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.type.name}: {self.url}'