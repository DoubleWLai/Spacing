from django.urls import path

from . import views

app_name = 'spacing'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    path('list/', views.list, name='list'),
    path('list/<int:id>', views.list_delete, name='list_delete'),
    path('update/<int:id>', views.update, name='update'),
]
