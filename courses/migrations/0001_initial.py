# Generated by Django 4.0.3 on 2022-06-01 10:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категорий')),
            ],
            options={
                'verbose_name': 'Категория курса',
                'verbose_name_plural': 'Категорий курсов',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название курса')),
                ('file', models.FileField(upload_to='media/%Y/%m/%d', verbose_name='PDF-Файл')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('stepic_link', models.URLField(blank=True, verbose_name='Ссылка курса на Stepic')),
                ('udemy_link', models.URLField(blank=True, verbose_name='Ссылка курса на Udemy')),
                ('my_link', models.URLField(blank=True, verbose_name='Ссылка на курс')),
                ('slug_course', models.SlugField(null=True, verbose_name='Слаг курса')),
                ('category_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category_course', verbose_name='Категория курса')),
                ('like', models.ManyToManyField(blank=True, related_name='like_course', to=settings.AUTH_USER_MODEL, verbose_name='Оценка курса')),
            ],
            options={
                'verbose_name': ('Курс',),
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.AddField(
            model_name='user_account',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='courses', to='courses.course', verbose_name='Записанные курсы'),
        ),
        migrations.AddField(
            model_name='user_account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user_account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
