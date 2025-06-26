from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='blog_images', blank=True, null=True)

    def __str__(self):
        return self.title
