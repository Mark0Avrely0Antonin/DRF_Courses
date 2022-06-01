from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User_Account(AbstractUser):
    courses = models.ManyToManyField('Course', verbose_name = 'Записанные курсы',
                                     blank = True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category_Course(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Название категорий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория курса'
        verbose_name_plural = 'Категорий курсов'


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'Создатель курса',
                             null = True)
    title = models.CharField(max_length = 255, verbose_name = 'Название курса')
    file = models.FileField(upload_to = 'media/%Y/%m/%d', verbose_name = 'PDF-Файл')
    description = models.TextField(verbose_name = 'Описание курса')
    category_course = models.ForeignKey(Category_Course, on_delete = models.CASCADE, verbose_name = 'Категория курса')

    stepic_link = models.URLField(verbose_name = 'Ссылка курса на Stepic', blank = True)
    udemy_link = models.URLField(verbose_name = 'Ссылка курса на Udemy', blank = True)
    my_link = models.URLField(verbose_name = 'Ссылка на курс', blank = True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name = 'Оценка курса',
                                   related_name = 'likes_course', blank = True)

    def __str__(self):
        return self.title




    class Meta:
        verbose_name = 'Курс',
        verbose_name_plural = 'Курсы'
