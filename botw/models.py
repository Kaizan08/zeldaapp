from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


class TimezoneChart(models.Model):
    name = models.TextField()
    hours = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=1024)
    fname = models.CharField(max_length=1024)
    lname = models.CharField(max_length=1024)
    email = models.EmailField()
    optIn = models.BooleanField(default=False)
    tc_agree_timestamp = models.DateTimeField(blank=True, null=True, editable=False)
    salt = models.CharField(max_length=1024, editable=False)
    hash = models.CharField(max_length=1024, editable=False)
    userTimezone = models.ForeignKey(TimezoneChart)
    createdDate = models.DateTimeField(default=timezone.now, editable=False)
    updatedDate = models.DateTimeField(default=timezone.now, editable=False)
    lastLoginDate = models.DateTimeField(editable=False, null=True)
    deleted = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.fname + ' ' + self.lname


class Type(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Set(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Quest(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    quest_name = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    type = models.ForeignKey(Type)
    set = models.ForeignKey(Set, blank=True, null=True)

    def __str__(self):
        return self.quest_name


class UserQuest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    quest = models.ForeignKey(Quest)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id


class Category(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    locations_found = models.CharField(null=True, blank=True, max_length=1024)
    rupee_val = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class ItemQuest(models.Model):
    item = models.ForeignKey(Item)
    quest = models.ForeignKey(Quest)
    quantity_required = models.IntegerField()


