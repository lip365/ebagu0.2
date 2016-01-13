import datetime
from haystack import indexes
from main.models import Category


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='name')
    
    def get_model(self):
        return Category

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()