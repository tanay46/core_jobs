import datetime
from haystack import indexes
from apps.jobs.models import *


class PostIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    modified_on = indexes.DateTimeField(model_attr='modified_on')

    def get_model(self):
        return Post

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(modified_on__lte=datetime.datetime.now())