from django.urls import path

from .views import *

urlpatterns = [
    path('courses/', List_API_Courses.as_view(), name='list_courses'),
    path('create_course/', Create_API_Course.as_view(), name='create_course'),
    path('update_course/<int:pk>/', Update_API_Course.as_view(), name='update_course'),

    path('retrieve_course/<int:pk>/', Retrieve_API_Course.as_view(), name='retrieve_course'),
]