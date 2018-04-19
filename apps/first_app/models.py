from django.db import models


class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First Name can't be empty"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last Name can't be empty"
        if len(postData['email']) < 1:
            errors['email'] = "Email can't be empty"
        return errors

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsersManager()