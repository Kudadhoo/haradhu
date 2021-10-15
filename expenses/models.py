from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ('Positive','Positive'),
    ('Negative','Negative'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField(null=True, blank=True)
    expenses = models.FloatField(default=0)
    balance = models.FloatField()


class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    expense_type = models.CharField(max_length=200, choices=TYPE)
    amount = models.FloatField()

    def __str__(self):
        return self.name
