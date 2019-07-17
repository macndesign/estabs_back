from django.urls import path, include
from .views import current_user, UserList, EstabelecimentoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'etabelecimentos', EstabelecimentoViewSet)

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('', include(router.urls)),
]
