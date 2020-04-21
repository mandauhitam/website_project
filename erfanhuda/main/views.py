#################################################################################################################################################
#                                 	   							WELCOME TO MY WEBSITES				                     						#
#                           	  							Authorized by Muhammad Erfan Huda					             					#
#                   							Created during COVID-19 Outbreak using Django and MongoDB       	         					#
#                              							HOPE PEOPLE ARE SAFE!!! STAY AT HOME!!!             	             					#
#################################################################################################################################################
from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, Categories, SeriesList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from PIL import ImageFile


# FINDING THE URL SINGLE_SLUG
# def single_slug(request, single_slug):
# 	categories = [c.url_slug for c in Categories.objects.all()]
# 	if single_slug in categories:
# 		matching_series = SeriesList.objects.filter(category__url_slug=single_slug)

# 		series_urls = {}
# 		for m in matching_series.all():
# 			part_one = Portfolio.objects.filter(series__series_name=m.series_name).earliest("published")
# 			series_urls[m] = part_one.url_slug

# 		return render(request,
# 					  "main/category.html",
# 					  {"part_ones": series_urls})

# 	portfolio = [p.url_slug for p in Portfolio.objects.all()]
# 	if single_slug in portfolio:
# 		this_portfolio = Portfolio.objects.get(url_slug = single_slug)
# 		return render(request,
# 					  "main/home.html",
# 					  {"portfolio": this_portfolio})
		
# 	return HttpResponse(f"{single_slug} does not correspond to anything.")


#HOMEPAGE with CATEGORIES
# def homepage(request):
# 	return render(request=request,
# 					template_name="main/categories.html",
# 					context={"categories": Categories.objects.all})

#HOMEPAGE
def homepage(request):
	return render(request=request,
					template_name="main/home.html",
					context={"portfolio": Portfolio.objects.all().order_by('-id')})

#ABOUT
def about(request):
	return render(request=request,
					template_name="main/about.html")

#USER REGISTER PAGE
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])

	form = UserCreationForm
	return render(request,	
				  "main/register.html",
				  context={"form":form})