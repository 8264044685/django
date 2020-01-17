from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path(r'^logins?/$',views.login,name= 'login'),
    re_path(r'^signup/$',views.signup,name= 'signup'),
    path('logout',views.logout_view,name='logout')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)