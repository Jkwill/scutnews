from django.db import models


class News(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    tag = models.ForeignKey(Section)
    article = models.TextField()
    subdate = models.DateField()
    readnum = models.IntegerField()


class Section(models.Model):
    name = models.CharField(max_length=10)


class Source(models.Model):
    id = models.ForeignKey(News, primary_key=True)
    name = models.CharField(max_length=10)
    # true = 文 false = 图
    job = models.BooleanField()


class Image(models.Model):
    id = models.ForeignKey(News, primary_key=True)
    image = models.ImageField()
