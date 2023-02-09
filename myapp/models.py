from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.title
