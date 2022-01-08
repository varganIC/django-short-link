from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('reg/', views.register, name='reg-page'),
    path('user/', authViews.LoginView.as_view(template_name='user/enter_user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='user/exit.html'), name='exit'),
    path('profile/', views.profile, name='profile'),
]
