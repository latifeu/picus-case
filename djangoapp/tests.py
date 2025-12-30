from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertIsNotNone(user.id)

    def test_user_name_max_length(self):
        user = User.objects.create(
            name="A" * 70,
            email="test2@example.com"
        )
        self.assertEqual(len(user.name), 70)

    def test_user_email_format(self):
        user = User.objects.create(
            name="Email Test",
            email="valid@email.com"
        )
        self.assertIn("@", user.email)

    def test_multiple_users(self):
        User.objects.create(name="User 1", email="user1@test.com")
        User.objects.create(name="User 2", email="user2@test.com")
        User.objects.create(name="User 3", email="user3@test.com")
        
        self.assertEqual(User.objects.count(), 3)

    def test_user_retrieval(self):
        user = User.objects.create(
            name="Retrieve Test",
            email="retrieve@test.com"
        )
        retrieved = User.objects.get(id=user.id)
        self.assertEqual(retrieved.name, "Retrieve Test")
        self.assertEqual(retrieved.email, "retrieve@test.com")

    def test_user_update(self):
        user = User.objects.create(
            name="Old Name",
            email="old@test.com"
        )
        user.name = "New Name"
        user.save()
        
        updated = User.objects.get(id=user.id)
        self.assertEqual(updated.name, "New Name")

    def test_user_deletion(self):
        user = User.objects.create(
            name="Delete Test",
            email="d@test.com"
        )
        user_id = user.id
        user.delete()
        
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=user_id)

    def test_user_filter_by_name(self):
        User.objects.create(name="A", email="ae@test.com")
        User.objects.create(name="B", email="b@test.com")
        
        alice = User.objects.filter(name="A").first()
        self.assertIsNotNone(alice)
        self.assertEqual(alice.email, "a@test.com")

    def test_user_filter_by_email(self):
        User.objects.create(name="Test", email="u@test.com")
        
        user = User.objects.filter(email="u@test.com").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "Test")