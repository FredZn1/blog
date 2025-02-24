from django.urls import path
from .views import AuthorListCreateView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
]
