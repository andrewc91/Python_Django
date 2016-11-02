from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validEmail(self, email):
        errors = []

        if len(email) < 1:
            errors.append('Please enter a email address!')

        if len(User.objects.filter(email=email)) > 0:
            errors.append('Email already in database!')

        if not EMAIL_REGEX.match(email):
            errors.append('Email is invalid! Try again!')

        if errors:
            return (False, errors)

        else:
            e = User.objects.create(email=email)
            return (True, e)

class User(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
