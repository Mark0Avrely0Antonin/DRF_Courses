from rest_framework import serializers

from .models import *


class Read_Course_Serialzier(serializers.ModelSerializer):
    category_course = serializers.ReadOnlyField(source = 'category_course.title')

    likes = serializers.SerializerMethodField(method_name = 'get_total_likes')

    def get_total_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'file', 'description', 'category_course', 'likes', 'stepic_link', 'udemy_link', 'my_link')


class Create_And_Update_Serializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(method_name = 'get_total_likes')

    def get_total_likes(self, obj):
        return obj.likes.count()


    class Meta:
        model = Course
        fields = ('title', 'file', 'description', 'category_course', 'likes', 'stepic_link', 'udemy_link', 'my_link')

