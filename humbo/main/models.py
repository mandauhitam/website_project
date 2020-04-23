from django.db import models
from django.utils import timezone

class Blog(models.Model):
	blog_title = models.CharField(max_length=200)
	blog_published = models.DatetimeField("date/time published", default = timezone.now())
	blog_content = models.TextField
	blog_image = models.FileField(upload_to = 'images/', null = True, blank=True)
	blog_video = models.FileField(upload_to = 'video/', null=True, blank=True, verbose_name="")

class Portfolio(models.Model):
	portfolio_title = models.CharField(max_length=200)
	portfolio_published = models.DatetimeField("date/time published", default = timezone.now())
	portfolio_content = models.TextField
	portfolio_image = models.FileField(upload_to = 'images/', null = True, blank=True)

class 