from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Event(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    date = models.DateField(null=True)
    participants = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        ordering = ['date']
