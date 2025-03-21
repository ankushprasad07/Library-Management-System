from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, AuthorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import RegisterView

# Create a router and register your viewsets
router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),  # Registration endpoint
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT obtain pair
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
]
