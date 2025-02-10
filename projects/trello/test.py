from django.test import TestCase
from django.contrib.auth.hashers import make_password , check_password
from rest_framework.exceptions import ValidationError
from membership.API.serializers import SignupSerializer, MemberSerializer 
from membership.models import MemberModel
from datetime import datetime

class SignupSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpassword123',
            'confirm_password': 'testpassword123',
            'email': 'testuser@example.com'
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

    def test_password_validation(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password'] = '12345678'  # Common password, should fail validation
        invalid_data['confirm_password'] = '12345678'
        serializer = SignupSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class MemberSerializerTest(TestCase):
    def setUp(self):
        self.member = MemberModel.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            password=make_password('testpassword123'),
            email='testuser@example.com'
        )

    def test_member_serialization(self):
        serializer = MemberSerializer(self.member)
        expected_data = {
            'id': self.member.id,
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com'
        }
        self.assertEqual(serializer.data, expected_data)

    def test_member_deserialization(self):
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com'
        }
        serializer = MemberSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        member = serializer.save()
        self.assertEqual(member.username, data['username'])
        self.assertEqual(member.first_name, data['first_name'])
        self.assertEqual(member.last_name, data['last_name'])
        self.assertEqual(member.email, data['email'])


