from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/create/', views.PhotoCreate.as_view(), name='photos_create'),
    # path('photos/', views.photos_index, name='index'),
    path('photos/upload/', views.upload_photo, name='upload_photo'),
]