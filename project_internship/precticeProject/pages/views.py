from django.shortcuts import render
from login.models import userProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
@login_required(login_url='/login/login')
def welcome(request):
    return render(request,'pages/welcome.html')
@login_required(login_url='/login/login')
def show_data(request):

    users = User.objects.all().select_related('userprofile')

    context = {
        'userData':users,

    }
    # for data in users:
        # print(data.userprofile.profilePicture.url)
    return render(request,'pages/show_data.html',context)