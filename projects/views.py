from django.shortcuts import render
from .models import Input

def portfolio_home(request):
    inputs = Input.objects
    return render(request, 'portfolio_home.html', {'inputs':inputs})
