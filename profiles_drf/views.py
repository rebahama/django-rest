from rest_framework import generics
from drf_api.permission import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer



class ProfileList(generics.ListAPIView):
    
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer
       

class ProfileDetail(generics.RetrieveUpdateAPIView):
    
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset=Profile.objects.all()