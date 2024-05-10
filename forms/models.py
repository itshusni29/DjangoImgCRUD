from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profiles

class TrainingRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_requests')
    title = models.CharField(max_length=200)
    participants = models.TextField()
    date = models.DateField()
    trainer = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    reason = models.TextField()
    manager = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name='mng')
    general_manager = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name='gm')
    attachments = models.ManyToManyField('Attachment', blank=True)

    def __str__(self):
        return self.title


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    
    def __str__(self):
        return self.file.name