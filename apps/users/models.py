from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
class SchoolUser(AbstractUser):
    # additional fields
    user_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=20)
    user_role = models.CharField(max_length=50, choices=[
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('employee', 'Employee'),
        ('staff', 'Staff'),
    ], default='student')
    present_address = models.TextField(blank=True, null=True)
    present_address = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')
    blood_group = models.CharField(choices=[
        ('a_positive', 'A+'),
        ('a_negative', 'A-'),
        ('b_positive', 'B+'),
        ('b_negative', 'B-'),
        ('ab_positive', 'AB+'),
        ('ab_negative', 'AB-'),
        ('o_positive', 'O+'),
        ('o_negative', 'O-')
    ])

    def __str__(self):
        return self.username