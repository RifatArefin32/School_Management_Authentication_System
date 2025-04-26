from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.

# `StudentUser` model, common for all types of users 
class SchoolUser(AbstractUser):
    user_id = models.IntegerField(unique=True, blank=True, null=True)  # allow blank and null
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
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')
    blood_group = models.CharField(max_length=20, choices=[
        ('a_positive', 'A+'),
        ('a_negative', 'A-'),
        ('b_positive', 'B+'),
        ('b_negative', 'B-'),
        ('ab_positive', 'AB+'),
        ('ab_negative', 'AB-'),
        ('o_positive', 'O+'),
        ('o_negative', 'O-')
    ], blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            last_user = SchoolUser.objects.order_by('-user_id').first()
            self.user_id = (last_user.user_id + 1) if last_user and last_user.user_id else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    
# `Student` specific properties for the students    
class Student(models.Model):
    user = models.OneToOneField(SchoolUser, related_name='student_profile', on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    study_class = models.CharField()
    section = models.CharField(max_length=100, blank=True, null=True)
    group = models.CharField(max_length=100, blank=True, null=True)
    shift = models.CharField(max_length=100, blank=True, null=True)
    session = models.CharField(max_length=50, blank=True, null=True)
    