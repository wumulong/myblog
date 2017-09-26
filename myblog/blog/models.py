from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name



class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	create_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag)
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title