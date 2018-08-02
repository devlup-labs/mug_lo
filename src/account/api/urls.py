from django.urls import path
from account.api.views import AuthenticationCheckAPIView

app_name = 'account'

urlpatterns = [
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check'),
]
