from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializer import User_serializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db import OperationalError, ProgrammingError


# Create your views here.

@api_view(["GET"])
def user_list(request):
    try:
        users = User.objects.all()
        serializer = User_serializer(users, many=True)
        return Response(serializer.data)
    except (OperationalError, ProgrammingError):
        return Response(
            {"error": "Database not ready"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

@api_view(['POST'])
def user_put(request):
    try:

        serializer = User_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "id": user.id
                },
                status=201
            )

        return Response(serializer.errors, status=400)
    except (OperationalError, ProgrammingError):
        return Response(
            {"error": "Database not ready"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )



@api_view(['GET'])
def user_get(request, id):
    try:

        user = get_object_or_404(User, id=id)
        serializer = User_serializer(user)
        return Response(serializer.data)
    except (OperationalError, ProgrammingError):
        return Response(
            {"error": "Database not ready"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )




@api_view(['DELETE'])
def user_delete(request, id):
    try:

        user = get_object_or_404(User, id=id)
        user.delete()
        return Response(status=204)
    except (OperationalError, ProgrammingError):
        return Response(
            {"error": "Database not ready"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )