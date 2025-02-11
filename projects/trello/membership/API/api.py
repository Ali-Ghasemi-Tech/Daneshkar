from .serializers import SignupSerializer , MemberSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView , RetrieveAPIView , ListAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import status , permissions 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , AllowAny 
from ..models import MemberModel 
from .permissions import IsSuperUserOrSelf , IsSelf , IsSuper , IsSuperUserOrNotAuthenticated
from ..backends import MemberAuthBackend
from django.contrib.auth import logout

class SignupApiView(ListCreateAPIView):
    serializer_class = SignupSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsSuperUserOrNotAuthenticated()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return MemberModel.objects.all()
        return MemberModel.objects.filter(id = self.request.user.id)

class DetailDeleteUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsSuperUserOrSelf]
     
class MemberListApiView(ListAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated] 

