from django.db import models

# Create your models here.

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     office = models.CharField(max_length=255)
#     age = models.IntegerField()
#     start_date = models.DateField()
#     salary = models.DecimalField(max_digits=10, decimal_places=2)

class NewsArticle(models.Model):
    headline = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='static/img/', blank=True)

    def __str__(self):
        return self.headline