from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # main app
    path('api/v1/main/', include('main.urls')),

    # worker app
    path('api/v1/worker/', include('worker.urls')),
    
    # company app
    path('api/v1/company/', include('company.urls')),

    # simple-jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
