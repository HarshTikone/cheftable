from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('signup/', views.signup_page, name="signup"),
    path('signin/', views.signin_page, name="signin"),
    path('post/', views.post_page, name="post"),
    path('explore/', views.explore_page, name="explore"),
    path('homeprofile/<str:username>/logout/', views.logout_page, name='logout'),
    path('homeprofile/<str:username>/', views.homeprofile_page, name='homeprofile'),
]



