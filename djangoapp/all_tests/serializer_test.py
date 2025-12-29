from django.test import TestCase
from djangoapp.serializer import User_serializer

class UserSerializerTests(TestCase):

    def test_valid_serializer_data(self):
   
        valid_data = {
            "name": "Ali abc",
            "email": "ali@example.com"
        }
        serializer = User_serializer(data=valid_data)
      
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], "Ali abc")

    def test_missing_email(self):
        
        invalid_data = {"name": "Ali aaa"}
        serializer = User_serializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_invalid_email_format(self):
        
        invalid_data = {"name": "Ali Veli", "email": "kkkkk-email"}
        serializer = User_serializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_name_max_length(self):
       
        long_name = "a" * 71
        invalid_data = {"name": long_name, "email": "ali@example.com"}
        serializer = User_serializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)