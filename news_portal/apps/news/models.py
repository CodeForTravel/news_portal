from hashlib import blake2s
from django.db import models


class Source(models.Model):
    source_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=255)
    language = models.CharField(max_length=5)
    country = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class TopHeadline(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=400, null=True, blank=True)
    title = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=400,null=True, blank=True)
    urlToImage = models.URLField(max_length=400,null=True, blank=True)
    publishedAt = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title