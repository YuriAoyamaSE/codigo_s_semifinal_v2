from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from contas.views.saldo_APIView import SaldoAPIView
from contas.views.transacao_APIView import TransacaoAPIView
from contas.views.transacao_viewset import TransacaoViewset
from contas.views.conta_viewset import ContaViewset


router = routers.DefaultRouter()
router.register(r'criarconta', ContaViewset)
router.register(r'criartransacao', TransacaoViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('conta/<int:pk>/saldo/', SaldoAPIView.as_view()),
    path('conta/transacao/', TransacaoAPIView.as_view()),
]
