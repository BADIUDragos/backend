from django.urls import path
from base.Auth.views import CustomTokenObtainPairView, blacklist_refresh_token
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist', blacklist_refresh_token, name="blacklist"),
    ]
