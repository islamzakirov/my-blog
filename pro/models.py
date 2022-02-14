from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField()
    like = models.BooleanField()
    publish_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
