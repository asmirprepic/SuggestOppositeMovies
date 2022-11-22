from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Movies"
    
def __str__(self):
    return self.movie_title