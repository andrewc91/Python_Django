from __future__ import unicode_literals

from django.db import models
import re, bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r"^[a-zA-Z\s]+$")

# Create your models here.
class LogUserManager(models.Manager):
    def register(self, input):
        errors = []

        if len(input['first_name']) < 2:
            errors.append('First name can not be fewer than 2 characters')

        if not name_regex.match(input['first_name']):
            errors.append('First Name can contain letters only')

        if len(input['last_name']) < 2:
            errors.append('Last name can not be fewer than 2 characters')

        if not name_regex.match(input['last_name']):
            errors.append('Last Name can contain letters only')

        if len(input['email']) < 1:
            errors.append('Must input email address')

        elif not email_regex.match(input['email']):
            errors.append('Email is invalid')

        same = LogUser.objects.filter(email=input['email'])
        if same:
            errors.append('Email already exists!')

        if len(input['password']) < 8:
            errors.append('Password must be at least 8 characters')

        if input['password'] != input['confirm']:
            errors.append('Passwords do not match')

        if len(errors) == 0:
            pwHash = bcrypt.hashpw(input['password'].encode(), bcrypt.gensalt().encode())
            #create new users
            user = LogUser.objects.create(first_name=input['first_name'], last_name=input['last_name'], email=input['email'], password=pwHash)
            return (True, user)
        else:
            return (False, errors)

    def login(self, input):
        errors = []
        if not input['email']:
            errors.append("Please enter email")

        if not input['password']:
            errors.append("Please enter password")

        user = LogUser.objects.filter(email=input['email'])
        if user.exists():
            inputPw = input['password'].encode()
            pwHash = user[0].password.encode()

            if bcrypt.checkpw(inputPw, pwHash):
                return (True, user[0])
            else:
                errors.append("No email and password match. Please try again")
                return (False, errors)
        else:
            errors.append("No email exists")
            return (False, errors)

class LogUser(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LogUserManager()
