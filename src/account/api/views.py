from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthenticationCheckAPIView(APIView):
    """
        get:
        Returns the authentication status code and message for current request.
    """

    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)
