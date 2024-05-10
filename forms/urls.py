from django.urls import path
from . import views

urlpatterns = [
    path('training-request/all/', views.all_training_requests, name='all_training_requests'),
    path('training-request/create/', views.create_training_request, name='create_training_request'),
    path('training-request/detail/<int:pk>/', views.training_request_detail, name='training_request_detail'),  # Corrected spelling of "detail"
    path('training-request/edit/<int:pk>/', views.edit_training_request, name='edit_training_request'),
    path('training-request/delete/<int:pk>/', views.delete_training_request, name='delete_training_request'),
]
