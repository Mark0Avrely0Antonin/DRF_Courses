from rest_framework import generics, permissions

from .models import *
from .serializers import *
from .permissions import *


class List_API_Courses(generics.ListAPIView):
    serializer_class = Read_Course_Serialzier
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Course.objects.filter()


class Create_API_Course(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Create_And_Update_Serializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class Update_API_Course(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = Create_And_Update_Serializer
    permission_classes = (Permission_Update_Course, permissions.IsAdminUser)


class Retrieve_API_Course(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = Read_Course_Serialzier
    permission_classes = (permissions.IsAuthenticated, Permission_Read_Course, )