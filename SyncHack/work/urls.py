from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
