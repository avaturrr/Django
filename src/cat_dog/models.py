from django.db import models


# Create your models here.
class AnimalImage(models.Model):
    url = models.URLField()
    spieces = models.CharField(default="cat", max_length=100, choices=[("cat", "Cat"), ("dog", "Dog")])
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(default="cat", max_length=5, choices=[("png", "png"), ("jpg", "jpg"), ("gif", "gif")])
