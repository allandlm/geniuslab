from django.db import models
from users.models import User
from books.models import Book

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('open', 'Aberto'), ('closed', 'Concluído')], default='open')

    def __str__(self):
        return f"Loan of {self.book.title} to {self.user.username}"