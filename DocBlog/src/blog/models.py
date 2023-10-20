from django.db import models
from django.contrib.auth.models import User  # Assurez-vous d'importer User depuis le bon emplacement
from django.utils import timezone

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisation de models. CASCADE comme exemple
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
