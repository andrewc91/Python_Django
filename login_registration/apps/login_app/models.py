from __future__ import unicode_literals

from django.db import models
import bcrypt, re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# name_regex = re.compile(r'^[A-Z][-a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, input):
        error = []

        if len(input['first_name']) < 2:
            error.append('First name canot be fewer than 2 characters')

        if len(input['last_name']) < 2:
            error.append('Last name can not be fewer than 2 characters')

        # if not name_regex.match(input['first_name']):
        #     error.append('Please enter letters only for first name')
        #
        # if not name_regex.match(input['last_name']):
        #     error.append('Please enter letters only for last name')

        if not email_regex.match(input['email']):
            error.append('Email is invalid')

        same = User.objects.filter(email=input['email'])
        if same:
            error.append('Email already in use')

        if len(input['password']) < 8:
            error.append('Password must be at least 8 characters')

        if input['password'] != input['confirm']:
            error.append('Passwords do not match. Try again')

        if len(error) == 0:
            pwHash = bcrypt.hashpw(input['password'].encode(), bcrypt.gensalt())
            e = User.objects.create(first_name=input['first_name'], last_name=input['last_name'], email=input['email'], password=pwHash)
            return (True, e)
        else:
            return (False, error)

    def loginValid(self, request):
        user = User.objects.filter(email=['email'])
        if user:
            user = user[0]
            if bcrypt.checkpw(input['password'].encode(), user.password.encode()):
                return (True, user)
        return (False, "Invalid email or password")


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
