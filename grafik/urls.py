from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart_data_list, name='chart_data_list'),
    path('create/', views.create_chart_data, name='create_chart_data'),
    path('update/<int:id>/', views.update_chart_data, name='update_chart_data'),
    path('delete/<int:id>/', views.delete_chart_data, name='delete_chart_data'),
]
