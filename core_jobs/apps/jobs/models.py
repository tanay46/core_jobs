from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    email = models.EmailField()
    description = models.CharField(max_length=4000)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    expires_on = models.DateField()
    slug = models.SlugField()
    tags = TaggableManager()

    def __unicode__(self):
        return ' '.join([self.title, str(self.created_on)])

    def tags_to_str(self):
        return ' '.join(map(lambda x: x.__str__(), self.tags.all()))

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Post, self).save(*args, **kwargs)