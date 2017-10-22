from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
# Create your views here.



def index(request):
	post_list = Post.objects.all().order_by('-create_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})



def detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
	post_list = Post.objects.filter(create_time__year=year, 
		                            create_time__month=month).order_by('-create_time')
	return render(request, 'blog/index.html', context={'post_list':post_list})


def category(request, pk):
	category_name = Category.objects.get(pk=pk)
	post_list = Post.objects.filter(category=category_name)

	return render(request, 'blog/index.html', context={'post_list':post_list})