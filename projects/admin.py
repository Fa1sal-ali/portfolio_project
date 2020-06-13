from django.contrib import admin

from .models import Input

admin.site.site_header = "Faisal's Portfolio & Blog Admin Console"

class InputAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary')

admin.site.register(Input, InputAdmin)