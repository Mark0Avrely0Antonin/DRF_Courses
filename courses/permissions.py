from rest_framework.permissions import BasePermission
from rest_framework import permissions


class Permission_Update_Course(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff or obj.user == request.user)


class Permission_Read_Course(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj in request.user.courses.all():
            return True
        else:
            return False
