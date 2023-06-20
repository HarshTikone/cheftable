from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('signup/', views.signup_page, name="signup"),
    path('signin/', views.signin_page, name="signin"),
    path('explore/', views.explore_page, name="explore"),
    path('<str:username>/profile/', views.profile, name='profile'),
    path('<str:username>/explore/', views.explore_page_user, name='explore1'),
    path('<str:username>/recipe/recipe/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('<str:username>/post/', views.post_page_user, name='post1'),
    path('<str:username>/logout/', views.logout_page, name='logout'),
    path('<str:username>/', views.homeprofile_page, name='homeprofile'),
]



