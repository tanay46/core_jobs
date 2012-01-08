from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    email = models.EmailField()
    description = models.CharField(max_length=4000)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    expires_on = models.DateField()
    tags = TaggableManager()

    def __unicode__(self):
        return ' '.join([self.title, str(self.created_on)])