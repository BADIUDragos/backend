from django.urls import path
from Auth.views import CustomTokenObtainPairView, validate_access_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('validate', validate_access_token, name='validate_access_token'),
    path('logout', TokenBlacklistView.as_view(), name="blacklist"),
    ]
