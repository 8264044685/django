from django.urls import path,include
# from account.views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns= [

    path('signup',views.signUp_view,name='signup'),
    path('login_view',views.login_View,name='login_view'),
    # path('signup',signUp_view.as_view(),name='signup'),
    # path('login_view/',login_view,name='login_view/')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)