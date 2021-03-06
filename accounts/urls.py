from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.home_view, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('write/',views.write, name='write'),
]