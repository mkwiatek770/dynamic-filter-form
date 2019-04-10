from django.urls import path
from core import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="articles"),
]
