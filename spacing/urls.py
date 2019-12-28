from django.urls import path

from . import views

app_name = 'spacing'
urlpatterns = [
    path('', views.index, name='index'),
    path('spacing/create/', views.create, name='create'),
    path('spacing/register/', views.register, name='register'),
    path('spacing/list/', views.list, name='list'),
    path('spacing/list/<int:id>', views.list_delete, name='list_delete'),
]
