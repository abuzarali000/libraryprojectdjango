from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    number_of_pages = models.IntegerField()
    book_cover = models.URLField(max_length=255)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title