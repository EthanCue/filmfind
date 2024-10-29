from django.db import models

# Create your models here.
class testTask(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    genres = models.TextField(max_length=255)
    original_language = models.CharField(max_length=10)
    release_date = models.DateField(null=True, blank=True)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    poster_path = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title