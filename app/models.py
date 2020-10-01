from django.db import models
from django.utils import timezone

class Thinkcentre(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email
    
    class Meta:
        verbose_name_plural = 'ThinkCentre'

class Thinkstation(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'ThinkStation'

class Thinkpad(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'ThinkPad'

class Esports(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'Esports'


class Campuscomputing(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'Campus Computing'


class Securityandservices(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'Security And Services'


class Datacentered(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Institution = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Email = models.EmailField(max_length=250)
    Country = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name_plural = 'Data Centered'