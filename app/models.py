from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Bookshelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', "Fiction"),
        ('nonfiction', "Nonfiction"),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    pages = models.IntegerField(default=0)
    category = models.CharField(max_length=25,choices=CATEGORY_CHOICES)
    bookshelves = models.ManyToManyField(Bookshelf, related_name='books')


