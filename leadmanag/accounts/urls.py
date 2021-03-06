from django.urls import path, include
from .resources import (
    RegisterView, LoginView, UserView
)
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterView.as_view(), name='register'),
    path('api/auth/login', LoginView.as_view(), name='login'),
    path('api/auth/user', UserView.as_view(), name='user'),
    path(
        'api/auth/logout',
        knox_views.LogoutView.as_view(),
        name="knox_logout"
    )
]
