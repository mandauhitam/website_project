##################################################################################################
#                                 	   WELCOME TO MY WEBSITES				                     #
#                           	  Authorized by Muhammad Erfan Huda					             #
#                   Created during COVID-19 Outbreak using Django and MongoDB       	         #
#                              HOPE PEOPLE ARE SAFE!!! STAY AT HOME!!!             	             #
##################################################################################################
from django.db import models
from django.utils import timezone

# Categories Model
class Categories(models.Model):
	category_name = models.CharField(max_length=200)
	category_image = models.FileField(null=True, blank=True)
	category_summary = models.CharField(max_length=200)
	url_slug = models.CharField(max_length=200, default=1)
 
# META DATA USED for ADMIN PAGE
	class Meta:
		verbose_name_plural = "Categories"

# Overriding the __str__ special method
# to make it a bit more readable when it's being displayed in string form, which we will see soon.
	def __str__(self):
		return self.category_name

# Series List Model
class SeriesList(models.Model):
	series_name = models.CharField(max_length=200)
	series_image = models.FileField(null=True, blank=True)
	category = models.ForeignKey(Categories, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

# META DATA USED for ADMIN PAGE
	class Meta:
		verbose_name_plural = "Series"

# Overriding the __str__ special method
# to make it a bit more readable when it's being displayed in string form, which we will see soon.
	def __str__(self):
		return self.series_name

# Portfolio Model
class Portfolio(models.Model):
	title = models.CharField(max_length=200)
	image = models.FileField(upload_to ='images/', null=True, blank=True)
	content = models.TextField()
	published = models.DateTimeField("date/time published",default=timezone.now())

# CONNECTING THE PORTFOLIO CONTENT TO THE SERIES
	series = models.ForeignKey(SeriesList, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)

# CUSTOMIZING URL_SLUG TO CONNECT TO CATEGORY
	url_slug = models.CharField(max_length=200, default=1)

# Overriding the __str__ special method
# to make it a bit more readable when it's being displayed in string form, which we will see soon.
	def __str__(self):
		return self.title