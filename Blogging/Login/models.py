from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     office = models.CharField(max_length=255)
#     age = models.IntegerField()
#     start_date = models.DateField()
#     salary = models.DecimalField(max_digits=10, decimal_places=2)



from django.utils import timezone

def get_image_upload_path(instance, filename):
    current_timestamp = timezone.now().timestamp()
    return f'media/{instance.slug}_{current_timestamp}_{filename}'

class NewsArticle(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('restaurant', 'Restaurant'),
        ('drink', 'Drink'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from ='headline',unique=True,null =True,default=None)
    description = models.TextField()
    date = models.DateField()
    image_url = models.URLField(max_length=100000,blank=True)
    image = models.ImageField(upload_to=get_image_upload_path, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.headline

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name