from rest_framework import generics, permissions
from drf_api.permission import IsOwnerOrReadOnly
from .models import Follower
from .seriealizer import FollowerSeriealizer


class Followerview(generics.ListCreateAPIView):
    serializer_class = FollowerSeriealizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Follower.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSeriealizer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    
