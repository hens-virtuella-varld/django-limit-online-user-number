from django.conf import settings
from django.db import models
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_in
from django.contrib.sessions.models import Session
from django.utils import timezone


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    last_visit = models.DateTimeField(null=True)


def active_user_session_number():
    return UserSession.objects.filter(
        last_visit__gte=timezone.now() - timezone.timedelta(seconds=settings.SESSION_COOKIE_AGE)
    ).count()

def user_logged_in_handler(sender, request, user, **kwargs):
    if active_user_session_number() >= settings.SESSION_COOKIE_AGE:
        return logout(request)


user_logged_in.connect(user_logged_in_handler)
