from django.db import models

from config.settings import AUTH_USER_MODEL


class Blog(models.Model):
    TYPES = {
        "Journal": 'Journal',
        "Life updates": "Life updates",
        "Travel": "Travel",
        "Personal development": "Personal development",
        "IT": "IT"
    }
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)  # lazy load
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='blog_images', blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPES, default="Journal")
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
