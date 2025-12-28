from rest_framework import serializers
from .models import User 
# serializer convert django model objects to json format for api
class User_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
