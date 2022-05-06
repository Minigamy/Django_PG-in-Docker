from django.contrib import admin
from django.urls import path

from bewise_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept_request),
]
