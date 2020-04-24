from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request=request,
				  	template_name="main/home.html")

def about(request):
	return HttpResponse('Berhasil About')

def blog(request):
	return HttpResponse('Checkpoint Berhasil')