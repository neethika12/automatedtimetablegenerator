# Generated by Django 5.1 on 2024-10-18 16:32

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('HeadOfDepartment', models.CharField(max_length=100)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('Venue', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('Course', models.CharField(max_length=5)),
                ('CourseCode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('CourseDescription', models.CharField(max_length=200)),
            ],
            options={
                'unique_together': {('Course', 'CourseCode')},
            },
        ),
        migrations.CreateModel(
            name='Instructor',
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
                ('FirstName', models.CharField(max_length=100, null=True)),
                ('MiddleName', models.CharField(max_length=100, null=True)),
                ('LastName', models.CharField(max_length=100, null=True)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructor',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableMain',
            fields=[
                ('YearOfStudy', models.CharField(max_length=9)),
                ('Programme', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Semister', models.CharField(max_length=100)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestart', models.TimeField()),
                ('TimeEnd', models.TimeField()),
                ('Day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=100)),
                ('RegisteredDate', models.DateTimeField(auto_now_add=True)),
                ('SessionType', models.CharField(choices=[('Tutorial', 'Tutorial'), ('Lecture', 'Lecture'), ('Lab', 'Lab'), ('Discussion', 'Discussion'), ('Presentation', 'Presentation')], max_length=100)),
                ('CourseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursename')),
                ('Programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.timetablemain')),
                ('Venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.venue')),
            ],
        ),
    ]
