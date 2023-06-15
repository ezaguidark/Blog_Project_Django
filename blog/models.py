from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey('auth.User',on_delete= models.CASCADE)

    def __str__(self):
        return self.title