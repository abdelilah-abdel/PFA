from django import forms  # For the authentification form
from django.shortcuts import redirect, render  # For rendering (displaying) our content
from .models import Quiz , category , questions  # To acquire the data from our models, then render it
from django.contrib.auth.models import User  # For verifying the user's given login info
from django.db.models import Q  # For searching based on multiple critereas
from django.contrib import messages  # For error flash messages 
from django.contrib.auth import authenticate , login , logout  # For user autentification (login/logout)
from django.contrib.auth.decorators import login_required # Forcing the user to login before doing something we specify
from django.contrib.auth.forms import UserCreationForm



# Login page
def loginPage(request):
    page = 'login'
    # Collecting login informations given by the user
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
    
    #if the user does not exist: 
        try:
            user = User.objects.get(username=username) 
        except:
            messages.error(request,'User does not exist')  

    #if the user exists:
        user = authenticate(request , username=username , password=password) #We verify his login infos 
    
    #if the infos are correct we log the user in and create a session:
        if user is not None:
            login(request , user)
            return redirect('index')

        else:
            messages.error(request,'Incorrect username or password')  
    context = {'page':page}
    return render(request,"quiz/login_register.html",context)

#user logout
def logoutUser(request):
    logout(request)
    return redirect('index')


# Registration page
def registerPage(request):
    form = UserCreationForm() #using the django generated registration form

    if request.method =='POST': #we collect the user's given data
       
        form = UserCreationForm(request.POST) #we pass it to the creation form
        
        if form.is_valid(): #we verify if the form is valid
            user = form.save(commit=False) 
            user.username = user.username.lower() #we lower the user's username
            user.save() #we save the user
            login(request,user) #we log the user in
            return redirect('index') #we redirect the user to the home page
            
        else:
            messages.error(request, 'An error occurred during your registration. Please try again.')        
    return render(request,'quiz/login_register.html',{'form':form})


def userProfile(request,pk):
    user = User.objects.get(id=pk)

    context = {'user':user}
    return render(request,"quiz/profile.html",context)





# home page
def index(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    quizs = Quiz.objects.filter(
        Q(category__name__icontains=q) |    
        Q(name__icontains=q) 
        )
    
    categorie = category.objects.all()

    return render(request , "quiz/index.html", {'quiz': quizs, 'category':categorie})


# Page with all categories
def categories(request):
    categorie = category.objects.all()
    return render(request , "quiz/categories.html",{'category':categorie})

# Page with each category and its quizzes
def category_(request,pk):
    categorie = category.objects.get(id=pk)
    quizs = Quiz.objects.all()
    return render(request, "quiz/category.html", {'category':categorie , 'quiz':quizs})

# page with each quiz
def quizzes(request,pk):
    question = questions.objects.all()
    quizs = Quiz.objects.get(id=pk)
    context = {'quiz':quizs ,'question':question}
    return render(request , "quiz/quizzes.html" , context)

