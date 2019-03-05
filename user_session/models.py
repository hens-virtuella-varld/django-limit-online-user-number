from django.conf import settings
from django.db import models

from django.contrib.auth.signals import user_logged_in
from django.contrib.sessions.models import Session
from django.utils.timezone import now


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    last_visit = models.DateTimeField(null=True)


def user_logged_in_handler(sender, request, user, **kwargs):
    UserSession.objects.update_or_create(
        user=user,
        session_id=request.session.session_key,
        defaults={'last_visit': now()}
    )


user_logged_in.connect(user_logged_in_handler)
