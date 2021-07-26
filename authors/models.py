from django.db import models


class Author(models.Model):
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50, blank=True)
  last_name = models.CharField(max_length=50)
  description = models.TextField(blank=True)

  def __str__(self):
    return f'{self.first_name}, {self.middle_name[0].upper() if self.middle_name else ""}. {self.last_name}'