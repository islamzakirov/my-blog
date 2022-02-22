from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField()
    like = models.BooleanField()
    publish_date = models.DateField(auto_now=True)
    tag = models.CharField(max_length=120)
    reyting = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name
