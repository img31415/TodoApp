from django.conf.urls import url, include
from django.contrib.auth.modesl import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields=['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objests.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlPattersm = {
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_frameworks.urls', namespace='rest_framework'))
}