from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
	return HttpResponse("a test")



def detail(request):
	return HttpResponse('detail page')