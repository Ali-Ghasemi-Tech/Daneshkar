from django.test import TestCase
from django.contrib.auth.hashers import make_password , check_password
from rest_framework.exceptions import ValidationError
from .API.serializers import SignupSerializer
from rest_framework.test import APITestCase , APIRequestFactory , APITransactionTestCase
from .models import MemberModel
from django.urls import reverse
from rest_framework import status
from django.test import TransactionTestCase

class SignupSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword123',
            'confirm_password': 'testpassword123',
            'email': 'testuser@example.com',
        }
    
   
    def test_valid_signup(self):
        serializer = SignupSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        member = serializer.save()
        self.assertEqual(member.username, self.valid_data['username'])
        self.assertEqual(member.first_name, self.valid_data['first_name'])
        self.assertEqual(member.last_name, self.valid_data['last_name'])
        self.assertEqual(member.email, self.valid_data['email'])
        self.assertTrue(member.check_password(self.valid_data['password']))

    def test_password_mismatch(self):
        invalid_data = self.valid_data.copy()
        invalid_data['confirm_password'] = 'wrongpassword'
        serializer = SignupSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_password_too_short(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password'] = 'short'
        invalid_data['confirm_password'] = 'short'
        serializer = SignupSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_password_too_common(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password'] = '12345678' 
        invalid_data['confirm_password'] = '12345678'
        serializer = SignupSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

# class MemberSerializerTest(TestCase):
#     def setUp(self):
#         self.member = MemberModel.objects.create(
#             username='testuser',
#             first_name='Test',
#             last_name='User',
#             password=make_password('testpassword123'),
#             email='testuser@example.com'
#         )

#     def test_member_serialization(self):
#         serializer = MemberSerializer(self.member)
#         expected_data = {
#             'id': self.member.id,
#             'username': 'testuser',
#             'first_name': 'Test',
#             'last_name': 'User',
#             'email': 'testuser@example.com'
#         }
#         self.assertEqual(serializer.data, expected_data)

#     def test_member_deserialization(self):
#         data = {
#             'username': 'newuser',
#             'first_name': 'New',
#             'last_name': 'User',
#             'email': 'newuser@example.com'
#         }
#         serializer = MemberSerializer(data=data)
#         self.assertTrue(serializer.is_valid())
#         member = serializer.save()
#         self.assertEqual(member.username, data['username'])
#         self.assertEqual(member.first_name, data['first_name'])
#         self.assertEqual(member.last_name, data['last_name'])
#         self.assertEqual(member.email, data['email'])

class SignupApiViewTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.superuser = MemberModel.objects.create_superuser(
            username = "admin",
            password = 'Adminpass1234'
        )

        self.normaluser = MemberModel.objects.create(
            username= 'testuser',
            password = 'Normaluser1234!'
        )

        self.url = reverse('signup_api')

    def test_superuser_list_view(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(len(response.data), 2)

    def test_normaluser_list_view(self):
        self.client.force_authenticate(user=self.normaluser)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_unauthenticated_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code , status.HTTP_403_FORBIDDEN)

    def test_superuser_create_accoount(self):
        self.client.force_authenticate(user=self.superuser)
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'Newuser1234!',
            'confirm_password': 'Newuser1234!',
            'email': 'user@example.com'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

    def test_normaluser_create_account(self):
        self.client.force_authenticate(user=self.normaluser)
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'Newuser1234!',
            'confirm_password': 'Newuser1234!',
            'email': 'user@example.com'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code , status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_create_account(self):
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'Newuser1234!',
            'confirm_password': 'Newuser1234!',
            'email': 'user@example.com'
            }
        response = self.client.post(self.url , data)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

class DetailDeleteApiViewTest(APITestCase):
    def setUp(self):
        self.superuser = MemberModel.objects.create_superuser(
            username = "admin",
            password = 'Adminpass1234'
        )

        self.normaluser = MemberModel.objects.create(
            username= 'testuser',
            password = 'Normaluser1234!'
        )

        self.seconduser = MemberModel.objects.create(
            username= 'seconduser',
            password = 'Normaluser1234!'
        )

        self.thirduser= MemberModel.objects.create(
            username= 'thirduser',
            password = 'Normaluser1234!'
        )

       

    def test_superuser_update_delete(self):
        
        self.client.force_authenticate(user=self.superuser)
        url = reverse('update_api' , kwargs={"pk" : self.seconduser.pk})
        data = {
            'username': 'updateUser',
            'first_name': 'update',
            'last_name': 'User',
            'email': 'Updateuser@example.com'
        }
        response = self.client.put(url , data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        response = self.client.delete(url)
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)

    def test_normaluser_update_delete(self):
        self.client.force_authenticate(user=self.normaluser)
        url = reverse('update_api' , kwargs={"pk" : self.normaluser.pk})
        data = {
            'username': 'updateUser',
            'first_name': 'update',
            'last_name': 'User',
            'email': 'Updateuser@example.com'
        }
        response = self.client.put(url , data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

        url = reverse('update_api' , kwargs={"pk" : self.thirduser.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code , status.HTTP_403_FORBIDDEN)
        response = self.client.delete(url)
        self.assertEqual(response.status_code , status.HTTP_403_FORBIDDEN)
        

class MemberListApiViewTest(APITestCase):
    def setUp(self):
        self.user = MemberModel.objects.create(
            username= 'testuser',
            password = 'testuser1234!'
        )

        self.url = reverse('member_list')


    def test_user_memberlist_view(self):
        self.client.force_authenticate(user = self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code , status.HTTP_200_OK)
    
    def test_nonauthuser_memberlist_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code , status.HTTP_403_FORBIDDEN)
    