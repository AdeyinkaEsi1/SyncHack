from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('', views.Signupview, name='register'),
    
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
