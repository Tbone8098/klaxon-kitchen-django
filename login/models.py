from django.db import models
import re
import bcrypt

# Create your models here.


class UserManager(models.Manager):
    def regi_user_validation(self, postData):
        errors = {}
        # areas to validate

        # confirm email not in system
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email_already_exists'] = "The email entered already exists"

        else:
            # name cannot be empty
            if len(postData['f_name']) == 0:
                # TODO make full name required using Regex
                errors['name'] = "First name is Required"

            if len(postData['l_name']) == 0:
                # TODO make full name required using Regex
                errors['name'] = "Last name is Required"

            # email must be correct structure
            EMAIL_REGEX = re.compile(
                r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = "Invalid email address"

            # password length
            if len(postData['pw']) < 8:
                # TODO use Regex to have password include cap, lower, special, num
                errors['pw'] = "Password must be more than 8 characters long"

            # confirm password match
            if postData['pw'] != postData['confirm-pw']:
                errors['confirm-pw'] = "Passwords do not match"

        return errors

    def login_validation(self, postData, user):
        # check if user exist
        errors = {}
        print(len(user))
        if len(user) > 0:
            pw_given = postData['pw']
            pw_hash = user[0].pw_hash

            print(bcrypt.checkpw(pw_given.encode(), pw_hash.encode()))

            if bcrypt.checkpw(pw_given.encode(), pw_hash.encode()) is False:
                print("password incorrect")
                errors['pw_incorrect'] = "password is incorrect"
        else:
            errors['invalid_user'] = "User does not exist"
        return errors

    def pw_hash(self, pw):
        # hash pw
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
        return pw_hash

    def check_pw(self, pw, confirm_pw):
        errors = {}
        if pw == confirm_pw:
            if len(pw) < 8:
                errors['pw_len'] = "password must be more than 8 characters long"
        else:
            errors['pw_match'] = "passwords do not match"
        return errors


class User(models.Model):
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    pw_hash = models.CharField(max_length=255)
    desc = models.TextField()
    user_level = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
