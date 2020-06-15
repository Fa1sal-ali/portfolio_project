from django.contrib import admin
from . models import post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time_stamp')

admin.site.register(post, PostAdmin)