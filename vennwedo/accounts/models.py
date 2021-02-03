from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, email, name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name="True",
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    objects = UserManager()

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.username
