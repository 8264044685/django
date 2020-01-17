from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields= ('username','email','password1','password2')

    # def clean_email(self):
    #         username = self.cleaned_data["username"]
    #         email = self.cleaned_data["email"]
    #         users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)
    #         if users:
    #             raise forms.ValidationError(("User with that email already exists."))
    #         return email.lower()

    

        
class ProfileForm(forms.ModelForm):
    # profilePicture = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    class Meta:
        model = userProfile
        fields = ('address','mobile_no','city','state','country','profilePicture')
