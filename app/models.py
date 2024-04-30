from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Price(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return f"{str(self.book.title)} - {str(self.price)}"
