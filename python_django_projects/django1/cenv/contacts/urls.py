from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<contact_id>',views.delete,name='delete'),
    path('edit/<contact_id>',views.edit,name='edit')
]