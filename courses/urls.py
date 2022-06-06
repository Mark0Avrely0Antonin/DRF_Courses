from django.urls import path

from .views import *

urlpatterns = [
    # users/ LIST GET / CREATE POST
    path('courses/', ListAPICourses.as_view(), name='list_courses'),
    path('create_course/', CreateAPICourse.as_view(), name='create_course'),
    # users/ID / DELETE /PATCH/PUT/ GET
    path('update_course/<int:pk>/', UpdateAPICourse.as_view(), name='update_course'),

    path('retrieve_course/<int:pk>/', RetrieveAPICourse.as_view(), name='retrieve_course'),
]