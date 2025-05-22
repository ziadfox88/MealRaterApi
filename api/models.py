from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import UniqueConstraint, Index


class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    # def __str__(self):
    #     return self.meal
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'meal'], name='unique_user_meal'),
        ]
        indexes = [
            Index(fields=['user', 'meal'], name='index_user_meal'),
        ]

