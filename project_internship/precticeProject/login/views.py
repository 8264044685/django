from django.shortcuts import render,redirect
from .form import SignUpForm,ProfileForm
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form.help_text = ''
        profileForm = ProfileForm(request.POST,request.FILES)


        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,'You are register can login in now')
            return redirect('login')
        else:
            messages.error(request,'Enter Right data')
            return redirect('signup')
    else:
        form = ProfileForm()
        profileForm = SignUpForm()
        context = {'form': form,'userProfileForm':profileForm,}
        return render(request,'login/signup.html',context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are login successfully")
            return redirect('welcome')
        else:
            messages.success(request, "Username and password are not match")
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')