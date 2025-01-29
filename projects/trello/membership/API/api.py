from .serializers import SignupSerializer , UpdateSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView
from ..models import MemberModel

class SignupApiView(ListCreateAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = SignupSerializer

class UpdateApiView(RetrieveUpdateAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = UpdateSerializer