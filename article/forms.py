from .models import article,comments
from django.forms import ModelForm
class ArticleForm(ModelForm):
    class Meta:
        model = article
        fields = ("title","text","article_image")
