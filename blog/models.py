from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey('auth.User',on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Por alguna razon, puede ser id o pk (id recomendado)
        return reverse("post_detail", args=[str(self.id)])
    