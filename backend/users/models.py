from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ('hr_officer', 'HR Officer'),
        ('hr_director', 'HR Director'),
        ('head', 'Department Head'),
        ('management', 'Management'),
        ('board', 'Board Member'),
        ('employee', 'Employee'),
        ('applicant', 'Job Applicant'),
        ('trainee', 'Graduate Trainee'),
        ('intern', 'Student Intern'),
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)    
