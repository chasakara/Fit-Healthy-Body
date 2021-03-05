from django.db import models

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
