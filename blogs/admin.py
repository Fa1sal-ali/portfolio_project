from django.contrib import admin
from . models import post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_time_stamp')

admin.site.register(post, PostAdmin)