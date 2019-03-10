from django.urls import path
from . import views

urlpatterns = [
    path('', views.active_user_session_number, name='active_user_session_number'),
]
