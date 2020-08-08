from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('',views.home_view, name='home'),
    path('add_view/',views.add_view, name='add_view'),
    path('mult_view/',views.mult_view, name='mult_view'),
    path('sub_view',views.sub_view, name='sub_view'),
]

