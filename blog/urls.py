from django.urls import path
from . import views

#add urls pattern
urlpatterns = [
    path('', views.post_list, name='post_list'),
]