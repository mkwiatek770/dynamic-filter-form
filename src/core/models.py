from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)
    published_date = models.DateField()
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
