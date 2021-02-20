from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('delete_user/<int:user_id>', views.delete_user),
    path('reset', views.reset)
]