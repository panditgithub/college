from django.urls import path
from .views import *
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",collegeIndex,name="home"),
    path('details',meeting_Details,name="meeting-details"),
    path('meetings',meetings,name="meetings"),
    path('register',user_register,name="register"),
    path('login',Login,name="login"),
    # path('results',results,name="results"),
    path('search/',search_user, name='search_user'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/', user_profile, name='user_profile'),
    path('logout/', signout, name="logout"),
]
