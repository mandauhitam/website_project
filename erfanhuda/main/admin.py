##################################################################################################################################################################################################################
#              															                   	   WELCOME TO MY WEBSITES				                     														 #
#                          															 	  Authorized by Muhammad Erfan Huda					             														 #
#                 															  Created during COVID-19 Outbreak using Django and MongoDB       	         														 #
#                              															HOPE PEOPLE ARE SAFE!!! STAY AT HOME!!!             	             													 #
##################################################################################################################################################################################################################
from django.contrib import admin
from .models import Portfolio, Categories, SeriesList
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
	fieldsets = [
		("Primary", {"fields":["published"]}),
		("URL", {"fields":["url_slug"]}),
		("Series", {"fields":["series"]}),
		("Image", {"fields":["image"]}),
		("Content", {"fields":["title", "content"]}),
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}	

#Register the site page of models
admin.site.register(SeriesList)
admin.site.register(Categories)
admin.site.register(Portfolio, PortfolioAdmin)