from django.db import models

# Create your models here.
class About(models.Model):
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(max_length=30, blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    aboutMe = models.TextField(blank=True, null=True)
    fackebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName

    class Meta:
        ordering = ["firstName", "-updated_at"]

class Experience(models.Model):

    title = models.CharField(max_length=100,  blank=True, null=True)
    companyName = models.CharField(max_length=70,  blank=True, null=True)
    aboutCompany = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=50,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.year

    class Meta:
        ordering = ["title", "year", "-updated_at"]

class Education(models.Model):
    name = models.CharField(max_length=200)
    dept = models.CharField(max_length=70, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)
    gpa = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", "group", "-updated_at"]

class Skill(models.Model):

    mySkill     = models.CharField(max_length=69,  blank=True, null=True)
    iKnow       = models.CharField(max_length=150, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.iKnow

    class Meta:
        ordering = ["iKnow", "-updated_at"]

class Interest(models.Model):

    myInterest  = models.TextField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.myInterest

    class Meta:
        ordering = ["myInterest", "-updated_at"]

class Award(models.Model):

    myAward     = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.myAward

    class Meta:
        ordering = ["myAward", "-updated_at"]