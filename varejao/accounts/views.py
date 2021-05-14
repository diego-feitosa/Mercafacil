from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import AccountSerializer
from django.contrib.auth.hashers import make_password


class AccountList(APIView):
    """
    List all Accounts or create a new Account
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        queryset = User.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = User()
        user.username = request.data['username']
        user.email = request.data['email']
        user.password = make_password(request.data['password'])
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        serializer = AccountSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
