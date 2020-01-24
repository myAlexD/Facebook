from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView 
from .models import Post, Comments
from django.http import JsonResponse, HttpResponse

class PostListView(ListView):
	model = Post 
	context_object_name = 'posts'
	class Meta:
		ordering = ["-date_posted"] 



def post_likes(request,pk):
	data = {}
	listUsers = ""
	try:
		user = request.user
		post = Post.objects.filter(id=pk).first()
	except:
		pass
	if user.is_authenticated:
		data["is_liked"] = user in post.liked_by.all()

		if user in post.liked_by.all():
			post.liked_by.remove(user)
		else:
			post.liked_by.add(user)
		data["like_count"] = int(Post.objects.filter(id=pk).first().liked_by.count())
		data["for"] = 'likes'
		data["post_id"] = str(pk)
		if data["like_count"] == 0:
			data["user_list"] = "No one liked this yet "
		else:
			for user_name in Post.objects.filter(id=pk).first().liked_by.all():
				listUsers += str(user_name) + ', '
			data["user_list"] = f"Liked by: { listUsers }"  
		return JsonResponse(data)
	else:
		return redirect('login')


def post_comment(request,pk):
	data = {}
	newComment = Comments()
	listUsers = ""
	try:
		user = request.user
		post = Post.objects.filter(id=pk).first()
	except:
		pass
	data["for"] = 'comments'
	if user.is_authenticated:
		newComment = Comments(post_k=post, comment=request.GET["comment_input"], user_c=user)
		newComment.save()
		data["post_id"] = str(pk)
		data["comment_count"] = str(Comments.objects.filter(post_k=post).first())
		return JsonResponse(data)
		print(data)
	else:
		return redirect('login')

def comment_section(request,pk):
	data = {}
	post = Post.objects.filter(id=pk).first()
	for x in range(Comments.objects.filter(post_k=post).count()):
		data[str(x)] = str(Comments.objects.filter(post_k=post).all()[x].comment)
		print(data)
	return JsonResponse(data,safe=False)


