from django.shortcuts import render
from django.http import HttpResponse

from user.models import *

# Create your views here.

def index(request):
    pass
    # return HttpResponse("Hello Django")
    return render(request, '')

def index2(request):
    return HttpResponse('Index2')

def get_users(request):
    
    users = UserModel.objects.all()
    
    # return HttpResponse(users)
    
    return render(request, 'users.html', {'users': users})