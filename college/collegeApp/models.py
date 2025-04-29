from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)




class UserManager(BaseUserManager):
    def create_user(self, email,username1, first_name= None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name
        ,username1=username1)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            username1=email
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username1=models.CharField(max_length=100,null=True,unique=True)
    first_name=models.CharField(max_length=100, null= True, blank = True)
    last_name=models.CharField(max_length=100,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    enrollment_number = models.CharField(max_length=20, unique=True,null=True)
    registration = models.CharField(max_length=100,null=True)
    valid = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=100,null=True)
    branch = models.CharField(max_length=100,null=True)
    year = models.IntegerField(null=True)
    phone = models.CharField(max_length=15, blank=True,null=True)
    profile_picture = models.ImageField(upload_to='media/student_profiles/', blank=True, null=True)
    # is_seller=models.BooleanField(default=False)
    # is_buyer=models.BooleanField(default=False)
    # is_verified=models.BooleanField(default=False)
    # is_online=models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"