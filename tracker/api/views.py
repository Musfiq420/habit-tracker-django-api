from rest_framework import viewsets, permissions
from ..models import Habit, HabitLog
from .serializers import HabitSerializer, HabitLogSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import AdminRenderer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            # Generate or retrieve the token for the logged-in user
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [AdminRenderer]

    def get_queryset(self):
        
        user = self.request.user
        
        return self.queryset.filter(user=user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitLogViewSet(viewsets.ModelViewSet):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [AdminRenderer]

    def get_queryset(self):
        return self.queryset.filter(habit__user=self.request.user)
