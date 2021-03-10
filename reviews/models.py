from django.db import models

# Create your models here.


class Reviews(models.Model):
    content = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
