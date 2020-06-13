from django.shortcuts import render
from .models import post

# Create your views here.
def allblogs(request):
    pst = post.objects
    return render(request, 'blog_home.html', {'pst':pst})