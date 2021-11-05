from django.db import models


class Idea(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        DONE = "DONE"
        ACCEPTED = "ACCEPTED"

    title = models.CharField(max_length=125)
    description = models.TextField()
    youtube_urk = models.URLField(null=True, blank=True)
    status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=45)


class Vote(models.Model):
    idea = models.ForeignKey(to=Idea, on_delete=models.CASCADE)
    reason = models.TextField()
