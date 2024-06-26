from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LogoutView, RegisterView, LoginView
from .views import EmployeeListView, ClientListView, CurrentUserView


app_name = 'accounts'

urlpatterns = [
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/current_user/', CurrentUserView.as_view(), name='current_user'),
    path('api/employees/', EmployeeListView.as_view(), name='employee_list'),
    path('api/clients/', ClientListView.as_view(), name='client_list'),
]
