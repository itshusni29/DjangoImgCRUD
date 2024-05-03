from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list),
    path('add/', views.image_upload),
    path('edit/<int:id>/', views.edit_image),
    path('delete/<int:id>/', views.delete_image),
    path('view/<int:id>/', views.view_image,),
]