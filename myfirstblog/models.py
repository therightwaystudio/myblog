from django.db import models


class Article(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.title