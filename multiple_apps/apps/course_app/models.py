from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models, IntegrityError

# Create your models here.
class CourseManager(models.Manager):
    def addUser(self, postData):
        try:
            this_course = self.get(id=postData['Course'])
            this_course.users.add(postData['User'])
        except IntegrityError:
            return False

class Course(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.TextField(max_length=255)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
