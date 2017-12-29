from django.db import models
from enquirer.models import Run


class Answer(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    index = models.IntegerField()
    value = models.IntegerField()
