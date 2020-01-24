from django.db import models
from django.contrib.auth.models import User
from time import time

class Post(models.Model):
	date_posted = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='newsfeed/media', blank=True)
	liked_by = models.ManyToManyField(User, related_name='number_of_likes', blank=True)

	def __str__(self):
		return self.title

	@property
	def total_likes(self):
		return self.liked_by.count


class Comments(models.Model):
	post_k = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
	comment = models.TextField()
	user_c = models.ForeignKey(User, on_delete=models.CASCADE, default='')
	commented_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'comment on {self.post_k}'
