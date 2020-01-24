from django import forms
from django.contrib.auth.models import User
from .models import Post, Comments
from django.forms import ModelForm

class Comment(ModelForm):
	class Meta:
		model = Comments
		fields = '__all__'