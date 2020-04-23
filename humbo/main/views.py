from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse('Berhasil')

def about(request):
	return HttpResponse('Berhasil About')

# Create your views here.
