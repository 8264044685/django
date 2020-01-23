from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

# from account.form import registration_form
from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as django_login, logout as django_logout, authenticate as django_authenticate
from . models import *



def signUp_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        mobile_no=request.POST['mobile_no']
        address=request.POST['address']

        if password1 == password2:

            if Account.objects.filter(email = email).exists():

                messages.error(request,"email is already taken")
                return redirect('signup')
            else:
                print("email is :--------- ",email)
                user = Account(username = username,email=email,city=city,address=address,state=state,country=country,mobile_no=mobile_no,password=password1)
                user.save()
                messages.success(request,"Account created successfuly")
                return redirect('login_view')
        else:
            return render(request, 'account/signup.html')
    return render(request,'account/signup.html')
def login_View(request):
    return render(request,'account/login.html')

# class login(View):
#
#     # @method_decorator(sensitive_post_parameters('password'))
#     # @method_decorator(csrf_protect)
#     # @method_decorator(never_cache)
# def login_view(request):
#     print("dispatch----")
#     if request.method == 'POST':
#         print("dispatch post----")
#         email = request.POST["email"]
#         print("email --",email)
#         password = request.POST["password"]
#         print("password --", password)
#         abc = Account.objects.filter(email=email).exists()
#         print("abc - ",abc, type(abc))
#         if abc:
#             print("dashboard")
#         else:
#             return render(request, 'account/login.html')
#     return render(request, 'account/login.html')
#
#         loginForm = login_form(request.POST)
#             print("login_form:", loginForm)
#
#             if loginForm.is_valid():
#                 print("valid form")
#                 return redirect('welcome')
#             else:
#                 print("not valid")
#                 return render(request, 'account/login.html',{'form':loginForm})
#         else:
#             loginForm = login_form()
#             return render(request, 'account/login.html',{'form':loginForm})
#         return render(request,'account/login.html')


