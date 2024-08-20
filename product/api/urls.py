from django.contrib import admin
from django.urls import include, path

from api.v1.views.user_view import UserViewSet

app_name = 'api'

urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
]
