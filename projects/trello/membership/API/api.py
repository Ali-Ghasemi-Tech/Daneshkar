from .serializers import SignupSerializer , MemberSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView , RetrieveAPIView , ListAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import status , permissions 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , AllowAny
from ..models import MemberModel 
from ..backends import MemberAuthBackend
from django.contrib.auth import logout

class SignupApiView(ListCreateAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = SignupSerializer

class DetailDeleteUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = MemberSerializer

# class LoginApiView(APIView):
#     queryset = MemberModel.objects.all()
#     serializer_class = LoginSerializer
#     permission_classes = [AllowAny]
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = MemberAuthBackend.authenticate(request, username=username, password=password)

#         if user:
#             # Authentication successful
#             return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             # Authentication failed
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class MemberListApiView(ListAPIView):
    queryset = MemberModel.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated] 

class LogoutApiView(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)