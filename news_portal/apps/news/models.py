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
    headline_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    urlToImage = models.URLField()
    publishedAt = models.DateTimeField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    urlToImage = models.URLField()
    publishedAt = models.DateTimeField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title