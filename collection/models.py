from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Collection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, related_name='book', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    page_number = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
