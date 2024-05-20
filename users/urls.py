from django.urls import path

from users.views import UserCreateView, UserProfileView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='api-token-auth'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserProfileView.as_view(), name='user-profile'),
]
