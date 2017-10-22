# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.models import Post

# Create your models here.


class Comment(models.Model):
	author = models.CharField(max_length=50)
	email = models.EmailField()
	body = models.TextField()
	post = models.ForeignKey(Post)
	url = models.URLField()
	created_time = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.body[:20]