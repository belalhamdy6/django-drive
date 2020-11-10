from django.db import models

# Create your models here.








class Book(models.Model):
    book_name    = models.CharField(max_length=50)
    author       = models.CharField(max_length=20)
    puplished_at = models.DateTimeField(auto_now_add=True)
    the_book     = models.FileField(upload_to="book/")
    about_book   =models.TextField(max_length=200)

    def __str__(self):
        return self.book_name



