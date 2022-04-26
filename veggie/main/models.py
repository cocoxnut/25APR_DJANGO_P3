from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'product/%Y/%m', blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'name: {self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self) -> str:
        return f'name: {self.name}'


class Category(models.Model):
    title = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

# Create your models here.
