from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<city_name>/',views.delete_city, name='delete_city'),
    url(r'^', views.index, name ='information'),
]
