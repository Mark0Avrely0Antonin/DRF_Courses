from django.urls import path

from courses.views import ListAPICourses, CreateAPICourse, UpdateAPICourse, DeleteAPICourse, RetrieveAPICourse


urlpatterns = [
    path('courses/', ListAPICourses.as_view(), name='list_courses'),
    path('create_course/', CreateAPICourse.as_view(), name='create_course'),
    path('update_course/<int:pk>/', UpdateAPICourse.as_view(), name='update_course'),
    path('delete_course/<int:pk>/', DeleteAPICourse.as_view(), name='delete_course'),
    path('retrieve_course/<int:pk>/', RetrieveAPICourse.as_view(), name='retrieve_course'),
]