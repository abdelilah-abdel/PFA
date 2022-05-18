from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [

    path('ss' , views.landing , name ="landing"),

    path('', views.index ,name="index" ),

    path('categories/',views.categories , name="categories"),

    path('quiz/<str:pk>/',views.quiz , name="quiz"),
    
    path('category/<str:pk>/' , views.category_,name="category"),

    path('login/',views.loginPage, name="login"),

    path('logout/',views.logoutUser, name="logout"),

    path('register/',views.registerPage, name="register"),

    path('profile/<str:pk>/',views.userProfile, name="profile"),

    path('search/',views.search , name="search"),

    path('allquizzes/' , views.allquizzes ,name="quizzes"),

    path('quiz/<str:pk>/data/' , views.quiz_data , name="quiz-data"),

    path('quiz/<str:pk>/save/' ,views.save_quiz , name="quiz-save" ),

    path('profile/<str:pk>/edit' , views.edit , name='edit'),
   
    path('form/',views.form, name="form"),

    path('profile/<str:pk>/history', views.history , name='history' )
    
]