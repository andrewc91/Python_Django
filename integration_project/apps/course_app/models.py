from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.TextField(max_length=255)
    users = models.ManyToManyField('login_app.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseUser(models.Model):
    user = models.ForeignKey('login_app.user', default = None)
    course = models.ForeignKey('course_app.course', default = None)
