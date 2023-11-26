from django.urls import path
from user.views import *

app_name = 'index'

urlpatterns = [
    # old write style
    # url(r'^index/', index)
    
    path("index/", index, name = "index"),
    path("index2/", index2, name = "index2"),
    path('users/', get_users, name = 'users')
    
]