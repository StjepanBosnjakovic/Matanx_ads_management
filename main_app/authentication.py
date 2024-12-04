from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import ExternalSystem

class ExternalSystemAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None

        # Expecting 'Token <token_value>'
        if not token.startswith('Token '):
            return None

        token_value = token.split(' ')[1]
        try:
            external_system = ExternalSystem.objects.get(token=token_value)
        except ExternalSystem.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        return (external_system, None)
