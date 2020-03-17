from django.db import models

# Create your models here.
from django.db import models
from datetime import date


class Member(models.Model):
    type = models.IntegerField()  # 0 : regular 1: admin
    name = models.CharField(max_length=100)


class Tasks(models.Model):
    # to-do title
    title = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.checked, self.created_at)
