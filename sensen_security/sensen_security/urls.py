from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from assessment.views import  send_password_reset_email


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assessment.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
