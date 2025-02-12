from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from membership.models import MemberModel
from .models import Workspace
from .API.serializer import WorkspaceCreateSerializer , WorkspaceUpdateDeleteSerializer , BoardSerializer , Board , TaskSerializer , TaskStatusUpdate , Task

class WorkspaceCreateSerializerTests(APITestCase):
    def setUp(self):
        self.owner = MemberModel.objects.create(
            username='owner',
            password='ownerpass123',

        )
        self.member1 = MemberModel.objects.create(
            username='member1',
            password='member1pass123'
        )
        self.member2 = MemberModel.objects.create(
            username='member2',
            password='member2pass123'
        )

    def test_serialization(self):
        workspace = Workspace.objects.create(
            name='Test Workspace',
            owner=self.owner,
            private=False,
            owner_id=self.owner.pk
        )
        workspace.members.set([self.member1, self.member2])
        serializer = WorkspaceCreateSerializer(workspace)
        self.assertEqual(serializer.data['name'], 'Test Workspace')
        self.assertEqual(serializer.data['owner'], self.owner.pk)
        self.assertIn('member1', serializer.data['members'])
        self.assertIn('member2', serializer.data['members'])

    def test_validation(self):
        data = {
            'name': '',  # Invalid: Name is required
            'owner': self.owner.pk,
            'private': False,
            'member_ids': [self.member1.pk, self.member2.pk]
        }
        serializer = WorkspaceCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

class WorkspaceUpdateDeleteSerializerTests(APITestCase):
    def setUp(self):
        self.owner = MemberModel.objects.create_user(
            username='owner',
            password='ownerpass123'
        )
        self.workspace = Workspace.objects.create(
            name='Test Workspace',
            owner=self.owner,
            private=True
        )

    def test_serialization(self):
        serializer = WorkspaceUpdateDeleteSerializer(self.workspace)
        self.assertEqual(serializer.data['name'], 'Test Workspace')
        self.assertEqual(serializer.data['owner'], 'owner')
        self.assertEqual(serializer.data['private'], True)

    def test_update(self):
        data = {
            'name': 'Updated Workspace',
            'private': False
        }
        serializer = WorkspaceUpdateDeleteSerializer(self.workspace, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        workspace = serializer.save()
        self.assertEqual(workspace.name, 'Updated Workspace')
        self.assertEqual(workspace.private, False)  


class BoardSerializerTests(APITestCase):
    def setUp(self):
        self.owner = MemberModel.objects.create_user(
            username='owner',
            password='ownerpass123'
        )
        self.workspace = Workspace.objects.create(
            name='Test Workspace',
            owner=self.owner,
            private=True
        )
        self.member1 = MemberModel.objects.create(
            username='member1',
            password='member1pass123'
        )
        self.member2 = MemberModel.objects.create(
            username='member2',
            password='member2pass123'
        )
        self.workspace.members.set([self.member1, self.member2])

    def test_serialization(self):
        board = Board.objects.create(
            name='Test Board',
            workspace=self.workspace
        )
        board.users.set([self.member1, self.member2])
        serializer = BoardSerializer(board, context={'members': self.workspace.members.all()})
        self.assertEqual(serializer.data['name'], 'Test Board')
        self.assertEqual(serializer.data['workspace'], self.workspace.pk)
        self.assertEqual(len(serializer.data['users']), 2)


class TaskSerializerTests(APITestCase):
    def setUp(self):
        self.owner = MemberModel.objects.create(
            username='owner',
            password='ownerpass123'
        )
        self.workspace = Workspace.objects.create(
            name='Test Workspace',
            owner=self.owner,
            private=True
        )
        self.board = Board.objects.create(
            name='Test Board',
            workspace=self.workspace
        )
        self.member1 = MemberModel.objects.create(
            username='member1',
            password='member1pass123'
        )
        self.board.users.set([self.member1])

    def test_serialization(self):
        task = Task.objects.create(
            title='Test Task',
            board=self.board,
            assigned_to=self.member1
        )
        serializer = TaskSerializer(task, context={'users': self.board.users.all()})
        self.assertEqual(serializer.data['title'], 'Test Task')
        self.assertEqual(serializer.data['board'], self.board.pk)
        self.assertEqual(serializer.data['assigned_to'], self.member1.pk)


    def test_validation_duplicate_title(self):
        Task.objects.create(
            title='Duplicate Task',
            board=self.board,
            description = 'text',
            assigned_to=self.member1,
            deadline = '2021-12-12'
        )
        data = {
            'title': 'Duplicate Task',
            'board': self.board.pk,
            'description': 'text',
            'assigned_to': self.member1.pk,
            'deadline': '2021-12-12'
        }
        serializer = TaskSerializer(data=data, context={'users': self.board.users.all()})
        self.assertFalse(serializer.is_valid())
        self.assertIn('task already exists.', serializer.errors)