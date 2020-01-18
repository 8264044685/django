from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    re_path(r'^logins?/$',views.login,name= 'login'),
    re_path(r'^signup/$',views.signup,name= 'signup'),
    path('logout',views.logout_view,name='logout'),
    path('pasword-reset/',auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),name='password_reset'),
    path('pasword-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),name='password_reset_done'),
    path('pasword-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'),name='password_reset_confirm'),
    path('pasword-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),name='password_reset_complete'),
    path('pasword-change/',auth_views.PasswordChangeView.as_view(template_name='login/password_change.html'),name='password_chane'),
    path('pasword-change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='login/password_change_done.html'),name='password_change_done'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)