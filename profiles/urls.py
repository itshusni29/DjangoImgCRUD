from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),  # Add a name to this URL pattern
    path('add/', views.profile_upload, name='add'),     # Add this line with the name 'add'
    path('edit/<int:id>/', views.edit_profile, name='edit'),
    path('delete/<int:id>/', views.delete_form, name='delete'),
    path('view/<int:id>/', views.view_profile, name='view'),
]
