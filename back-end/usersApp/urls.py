from django.urls import path
from .views import *
urlpatterns = [
    path('', getAllUsers, name='getAllUsersRoute'),
    path('add/', addUser, name="addUserRoute"),
]