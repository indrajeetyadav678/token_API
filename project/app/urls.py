from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework import routers
from .views import* 

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token)
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # this line is used for only login & logout feature in DRF window
]