from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index ,name="index" ),

    path('categories/',views.categories , name="categories"),

    path('quizzes/<str:pk>',views.quizzes , name="quizzes"),
    
    path('category/<str:pk>' , views.category_,name="category"),

    path('login/',views.loginPage, name="login"),

    path('logout/',views.logoutUser, name="logout"),

    path('register/',views.registerPage, name="register"),

    path('profile/<str:pk>/',views.userProfile, name="profile"),


]