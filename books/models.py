from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    total_quantity = models.PositiveIntegerField()
    available_quantity = models.PositiveIntegerField()
    description = models.TextField(default="Sem descrição.")
    
    def __str__(self):
        return f"{self.title} by {self.author}"