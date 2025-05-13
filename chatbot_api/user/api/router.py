from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.api.views import RegisterView, CurrentView, UserListView, UserView

urlpatterns = [
    path('auth/current/', CurrentView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('user/', UserListView.as_view()),
    path('user/<int:id>', UserView.as_view()),
]
