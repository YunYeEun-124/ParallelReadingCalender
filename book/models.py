from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    total_page = models.IntegerField(default=0)
    now_page = models.IntegerField(default=0)
    cover = models.ImageField(blank=True,upload_to='book_covers/')
    done = models.BooleanField(default = False) #완독은 트루, 아니면 false
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    comments = models.JSONField()

    def __str__(self):
        return self.title
