from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    """
    docstring
    """
    def __str__(self):
        """
        docstring
        """
        return "@{}".format(self.username)