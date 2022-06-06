from rest_framework import generics, permissions

from courses.models import Course
from courses.serializers import ReadCourseSerialzier, CreateAndUpdateSerializer
from courses.permissions import PermissionReadCourse, PermissionUpdateCourse


class ListAPICourses(generics.ListAPIView):
    serializer_class = ReadCourseSerialzier
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Course.objects.filter()


class CreateAPICourse(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateAndUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class UpdateAPICourse(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateAndUpdateSerializer
    permission_classes = (PermissionUpdateCourse, )


class RetrieveAPICourse(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = ReadCourseSerialzier
    permission_classes = (PermissionReadCourse, )