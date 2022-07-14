from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from contas.views import ContaViewset


router = routers.DefaultRouter()
#router.register(r'contas', ContaViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
