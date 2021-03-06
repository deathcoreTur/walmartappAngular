from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from .models import UserProfile
from .permissions import IsProfileOwner
from .serializers import UserProfileSerializer

class MyProfileViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsProfileOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            UserProfile.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


