from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home-page'),
    path('contact', views.contact, name='contact-page'),
    path('short', views.CreateLink.as_view(), name='short-page'),
    path(f'{settings.SITE_URL}/<slug:pk>', views.redirect_original, name='redirectoriginal'),
]
