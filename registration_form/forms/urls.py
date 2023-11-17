from django.urls import path

from . import views


urlpatterns = [
    path('', views.add_forms, name='add_forms'),
]
