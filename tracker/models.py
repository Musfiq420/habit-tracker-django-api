from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    question = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_value = models.PositiveIntegerField(blank=True, null=True)
    target_day = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="logs")
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()

    class Meta:
        unique_together = ('habit', 'date', 'user')

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {self.value} for {self.user.username}"