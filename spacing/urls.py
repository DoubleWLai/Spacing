from django.urls import path

from . import views

app_name = 'spacing'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),

]
