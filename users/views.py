from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserRegisterSerializer
from users.models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

