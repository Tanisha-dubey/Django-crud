from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('query',views.query,name="query"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:x>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('logout/', views.logout_view, name='logout'),
    path('all_data/', views.all_data, name='all_data'),  # New path for all data
]
