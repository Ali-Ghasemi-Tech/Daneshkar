from .serializers import SignupSerializer , UpdateSerializer , LoginSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import MemberModel
from ..backends import MemberAuthBackend

class SignupApiView(ListCreateAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = SignupSerializer

class UpdateApiView(RetrieveUpdateAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = UpdateSerializer

class LoginApiView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = MemberAuthBackend.authenticate(request, username=username, password=password)

        if user:
            # Authentication successful
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)