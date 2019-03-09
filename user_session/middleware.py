from django.utils.timezone import now

from .models import UserSession


class SetLastVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        if request.user.is_authenticated:
            # Update last visit time after request finished processing.
            UserSession.objects.update_or_create(
                user=request.user,
                session_id=request.session.session_key,
                defaults={'last_visit': now()}
            )

        return response
