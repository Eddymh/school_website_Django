# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register (self,post_data):
        errors=[]
        if len(post_data["first_name"])<1:
            errors.append("First name is required")
        elif len(post_data["first_name"])<2:
            error.append("First name must be at least 2 characters long")

        if len(post_data["last_name"])<1:
            errors.append("Last name is required")
        elif len(post_data["last_name"])<2:
            error.append("Last name must be at least 2 characters long")

        if len(post_data["email"])<1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(post_data["email"]):
            errors.append("Invalid email")
        else:
            users_with_matching_email = User.object.filter(email=post_data["email"].lower())
            if len(users_with_matching_email)>0:
                errors.append("Email already exists")

        if len(post_data["password"])<1:
            errors.append("Password is required")
        elif len(post_data["password"])<8:
            errors.append("Password needs to be 8 or more characters long")

        if len(post_data["confirm"])<1:
            errors.append("Password confirmation is required")
        elif post_data["password"] != post_data["confirm"]:
            errors.append("Confirm Password must match Password")

        if len(post_data["date_of_birth"])<1:
            errors.append("Date of birth is required")
        else:
            dob = datetime.strptime(post_data["date_of_birth"], "%Y-%m-%d")
            if dob > datetime.now():
                errors.append("Date of Birth must be in the past")

        if len(errors)>0:
            return (False,errors)
        else:
            user = User.objects.create(
                first_name=post_data["first_name"],
                last_name=post_data["last_name"],
                email=post_data["email"],
                password=bcrypt.checkpw(post_data["password"].encode(),bcrypt.gensalt()):
                date_of_birth=dob
            )
            return (true,user)

class User(models.Model):
    first_name = models.Charfield(max_length=255)
    last_name = models.Charfield(max_length=255)
    email = models.Charfield(max_length=255)
    password = models.charfield(max_length=255)
    date_of_birth = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager();
