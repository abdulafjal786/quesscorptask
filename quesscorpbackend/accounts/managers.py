from django.contrib.auth.models import BaseUserManager, PermissionsMixin




class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        email=self.normalize_email(email)
        user=self.model(username=username,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password):
        user=self.create_user(username,email,password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user