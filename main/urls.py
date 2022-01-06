

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index-admin'),
    path('user-page/', userpage, name="user-page"),
    path('createsubuser/', createsubuser, name="user-page"),
]
