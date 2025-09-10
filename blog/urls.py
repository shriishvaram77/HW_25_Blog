from django.urls import path

from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView, ArticleListView,ContactUsView

app_name = 'blog'

urlpatterns = [

    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_details'),
    path('articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('contacts/', ContactUsView.as_view(), name='contacts'),
]