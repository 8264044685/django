from django.urls import path,include
# from pages.views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    # path('',My_index_view.as_view(),name='index'),
    # path('welcome',welcome_view.as_view(),name='welcome'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)