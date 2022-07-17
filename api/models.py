from django.db import models

# Create your models here.


class user_details(models.Model):
    username = models.CharField(max_length=30)
    level = models.IntegerField()
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    gameType = models.CharField(max_length=15)
    duration = models.DateTimeField(auto_now=False)
    timestamp = models.DecimalField(max_digits=17, decimal_places=7)
    sync = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}, {self.level}, {self.stars}'
