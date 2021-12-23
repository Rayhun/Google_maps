from django.urls import path
from . import views
urlpatterns = [
    path('', views.ImageUpload.as_view(), name='image_upload'),
]
