from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_orders, name='add-orders'),
    path('all/', views.view_orders, name='view_orders'),
    path('update/<int:pk>/', views.update_orders, name='update-orders'),
    path('order/<int:pk>/delete/', views.delete_orders, name='delete-orders'),
    path('order/<int:pk>', views.order_details, name='order-details'),
    path('courier_my_orders/', views.courier_my_orders, name='courier-my_orders'),
    path('customer_my_orders/', views.customer_my_orders, name='customer-my-orders'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegistrationView.as_view(), name='registration'),
]