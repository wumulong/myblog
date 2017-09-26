from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.



def index(request):
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', context={'post_list': post_list})



def detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/detail.html', context={'post': post})