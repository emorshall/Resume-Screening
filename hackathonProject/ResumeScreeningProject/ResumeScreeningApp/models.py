from django.db import models


# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


class ResumeProfile(models.Model):
    profile_name = models.CharField(max_length=100)
    profile_keyword = models.TextField()
    active = models.BooleanField()


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    active = models.BooleanField()


class CandidateProfile(models.Model):
    can_name = models.CharField(max_length=100)
    can_email = models.CharField(max_length=100)
    can_contact = models.CharField(max_length=15)
    can_skills = models.TextField()
    can_status = models.FloatField(default=0.0)
    active = models.BooleanField()
    created_date = models.DateField()
