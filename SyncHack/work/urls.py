from django.urls import path
from . import views


urlpatterns = [
    path('', views.WelcomeView, name='home'),
    path('register', views.Signupview, name='register'),
    
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
