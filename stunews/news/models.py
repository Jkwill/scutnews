# coding utf-8
from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    tag = models.ForeignKey(Section)
    article = models.TextField(max_length=100)
    subdate = models.DateField()
    readnum = models.IntegerField()

    def __str__(self):
        return self.title


class Source(models.Model):
    tid = models.ForeignKey(News)
    name = models.CharField(max_length=10)
    # true = 文 false = 图
    job = models.BooleanField()

    def __str__(self):
        return self.name


# class Image(models.Model):
#     mid = models.ForeignKey(News)
#     # image = models.ImageField()
#
#     def __str__(self):
#          return self.image
