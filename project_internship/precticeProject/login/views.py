from django.shortcuts import render,redirect,Http404

from .form import SignUpForm,ProfileForm
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control



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

    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=request.POST['username'])
        request.session['username'] = user.username
        user = auth.authenticate(username=username,password=password)
        # print("session username ==>",user)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are login successfully")
            return redirect('welcome')
        else:
            messages.error(request, "Username and password are not match")
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'login/login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    auth.logout(request)
    return render(request, 'pages/index.html')
