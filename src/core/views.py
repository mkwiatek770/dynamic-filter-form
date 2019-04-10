from django.shortcuts import render
from django.views.generic import ListView
from core.models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles.html"

    def get_queryset(self):
        qs = Article.objects.all()
        return qs
