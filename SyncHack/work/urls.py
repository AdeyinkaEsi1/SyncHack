from django.urls import path
from . import views


urlpatterns = [
    path('', views.WelcomeView, name='home'),
    path('register', views.RegisterView, name='register'),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name='logout'),
    path('dashboard/', views.DashboardView, name="dashboard"),
    path('dashboard/admin', views.AdminDashboardView, name="admin_dashboard"),
    path('users/', views.AddUserView, name="add_user"),
    
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
