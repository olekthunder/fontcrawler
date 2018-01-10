from django.contrib.auth.models import User
from django.db import models


class Font(models.Model):
    user = models.ForeignKey(User, related_name='fonts',
                             on_delete=models.CASCADE, null=True)
    family = models.CharField(max_length=90, blank=True)
    url = models.URLField()
    style = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.family
