from __future__ import unicode_literals
from django.db import models
import bcrypt


class UserManager(models.Manager):

    def validate(self, post):
        errors = []
        if len(post['f_name']) < 3:
            errors.append('Name must be at least 3 characters long')
        if not post['f_name'].isalpha():
            errors.append('Name can only contain letters')
        if len(post['l_name']) < 3:
            errors.append('Name must be at least 3 characters long')
        if not post['l_name'].isalpha():
            errors.append('Name can only contain letters')
        if len(post['username']) < 3:
            errors.append('Username must be at least 3 characters long')
        if len(post['pw']) < 8:
            errors.append('password must be at least 8 characters long')
        if post['pw'] != post['pwconf']:
            errors.append('password and confirmation fields do not match')
        if post['phone_one'].isalpha():
            errors.append('Phone number can only contain digits')
        if post['phone_two'].isalpha():
            errors.append('Phone number can only contain digits')
        if post['phone_three'].isalpha():
            errors.append('Phone number can only contain digits')
        check_user = self.filter(username=post['username'])
        if check_user:
            errors.append('Username already exist in the database')
        return errors

    def signin(self, post):
        errors = []
        if len(post['username']) < 3:
            errors.append('username must be at least 3 characters long')
        elif len(post['pw']) < 8:
            errors.append('password must be at least 8 characters long')
        else:
            username = post['username']
            check_user = self.filter(username=post['username'])
            if not check_user:
                errors.append('no such user in database')
            else:
                pw_check = self.get(username=post['username'])
                pw = bcrypt.hashpw(post['pw'].encode(),
                                   pw_check.password.encode())
                if pw != pw_check.password:
                    errors.append('Incorect Password for user')
                else:
                    pass
        return errors


class TruckManager(models.Manager):

    def validate(self, post):
        errors = []
        if len(post['prod_name']) < 1:
            errors.append('Field may not be empty')
        if len(post['prod_name']) < 3:
            errors.append(
                'Product/Item name must be at least 3 characters long')
        check_product = self.filter(prod_name=post['prod_name'])
        if check_product:
            errors.append('Product already exist in the database')
        return errors


# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=455)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Truck(models.Model):
    user = models.ForeignKey('User',related_name="truck")
    category = models.ForeignKey('Category', related_name="truck")
    document = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = TruckManager()

class Color(models.Model):
    primary_color = models.CharField(max_length=255)
    secondary_color = models.CharField(max_length=255)
    truck_color = models.ForeignKey('Truck', related_name="color")
