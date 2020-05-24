from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve as _server

def serve(request, path):
    if "." not in path:
        path = "index.html"
    return _server(request, path, '/vue')

urlpatterns = [
    path('api/', include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r"(?P<path>(^/?$|.*\.(js|css)))", serve),
]
