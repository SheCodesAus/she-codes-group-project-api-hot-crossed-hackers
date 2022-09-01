
from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.view import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scholarships.urls')),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
