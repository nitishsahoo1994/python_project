from django.contrib import admin
from testapp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','body','author','publish','created','updated','status',]
    prepopulated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','email','comment','created','updated','active']
    search_fields = ["name","email"]

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


