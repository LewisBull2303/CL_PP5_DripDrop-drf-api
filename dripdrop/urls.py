# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView


# Internal:
from .views import home, logout_route
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),
    path('followers/', include('followers.urls')),
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]