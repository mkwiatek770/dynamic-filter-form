from django.shortcuts import render
from django.views.generic import ListView
from core.models import Article
from django.db.models import Q


def condition_valid(param):
    return param != "" and param is not None


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles.html"

    def get_queryset(self):
        request = self.request

        title_contains = request.GET.get("title_contains")
        id_exact = request.GET.get("id_exact")
        title_or_author = request.GET.get("title_or_author")
        view_count_min = request.GET.get("view_count_min")
        view_count_max = request.GET.get("view_count_max")
        date_min = request.GET.get("date_min")
        date_max = request.GET.get("date_max")
        category = request.GET.get("category")

        qs = Article.objects.all()

        if condition_valid(title_contains):
            qs = qs.filter(title__icontains=title_contains)
        elif condition_valid(id_exact):
            qs = qs.filter(id=id_exact)
        elif condition_valid(title_or_author):
            qs = qs.filter(Q(title__icontains=title_or_author)
                           | Q(author__name__icontains=title_or_author))

        if condition_valid(view_count_min):
            qs = qs.filter(views__gte=int(view_count_min))

        if condition_valid(view_count_max):
            qs = qs.filter(views__lte=int(view_count_max))

        return qs
