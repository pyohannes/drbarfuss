import datetime
import random
from django.db import models
from django.contrib.auth.models import User


def _random_hash():
    return hex(random.randint(10**20, 10**24))[2:]


class Test(models.Model):
    module = models.CharField(max_length=50)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    needs_birth = models.BooleanField(default=False)
    needs_sex = models.BooleanField(default=False)


class Run(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=32, default=_random_hash)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    issued = models.DateField(default=datetime.date.today)
    finished = models.DateField(blank=True, null=True)
    iv_id = models.CharField(max_length=256)
    iv_birth = models.DateField(blank=True, null=True)
    iv_male = models.BooleanField(default=True)
