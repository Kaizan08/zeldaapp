from django.db import models
from django.utils import timezone
import uuid

class TimezoneChart(models.Model):
    name = models.TextField()

class Users(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField()
    fname = models.TextField()
    lname = models.TextField()
    email = models.EmailField()
    optIn = models.BooleanField(default=False)
    tc_agree_timestamp = models.DateTimeField(blank=True, null=True)
    salt = models.TextField()
    hash = models.TextField()
    userTimezone = models.ForeignKey(TimezoneChart)
    createdDate = models.DateTimeField(default=timezone.now)
    updatedDate = models.DateTimeField(default=timezone.now)
    lastLoginDate = models.DateTimeField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username + ' ' + self.email + ' optIn=' + self.optIn
class Type(models.Model):
    name = models.TextField()

class Quests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quest_name = models.TextField()
    description = models.TextField()
    link = models.URLField()
    type_id = models.ForeignKey(Type)

class UserQuests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users)
    quest_id = models.ForeignKey(Quests)
    completed = models.BooleanField(default=False)

class Category(models.Model):
    name = models.TextField()

class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    description = models.TextField(null=True)
    locations_found = models.TextField(null=True)
    rupee_val = models.FloatField(null=True)
    category_id = models.ForeignKey(Category)

class ItemQuests(models.Model):
    item_id = models.ForeignKey(Items)
    quest_id = models.ForeignKey(Quests)
    quantity_required = models.IntegerField()
