from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('account/', include('account.api.urls', namespace='account')),
]
