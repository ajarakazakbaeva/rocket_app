from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_orders, name='add-orders'),
    path('all/', views.view_orders, name='view_orders'),
    path('update/<int:pk>/', views.update_orders, name='update-orders'),
    path('order/<int:pk>/delete/', views.delete_orders, name='delete-orders'),

]