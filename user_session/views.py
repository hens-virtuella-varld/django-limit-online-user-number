from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse

from .models import UserSession


def active_user_session_number(request):
    user_session_number = UserSession.objects.filter(last_visit__gte=timezone.now() - timezone.timedelta(minutes=1)).count()
    return HttpResponse(user_session_number)
