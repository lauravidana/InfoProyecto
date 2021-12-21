from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'contenido', 'fecha_creacion')
	list_filter = ('titulo','contenido','fecha_creacion')

# Register your models here.
admin.site.register(Post, PostAdmin)
