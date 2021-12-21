from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Post

class ListarPosts(ListView):
	model = Post
	template_name = "posts/postsList.html"
	context_object_name = "posts"
	#def get_queryset(self):
	#	noticias = Noticia.objects.all().order_by('-fecha_creacion')
	#	return noticias