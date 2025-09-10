from .models import Blogpost
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ArticleListView(ListView):
    model = Blogpost
    template_name = 'blog/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        return Blogpost.objects.filter(is_published=True)


class ArticleCreateView(CreateView):
    model = Blogpost
    fields = ['title', 'description']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:articles')


class ArticleDetailView(DetailView):
    model = Blogpost
    template_name = 'blog/article_details.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        # Retrieve the object using the parent's get_object method
        obj = super().get_object(queryset)

        # Safely increment the view count using an F() expression
        obj.views_count = F('number_of_views') + 1
        obj.save(update_fields=['number_of_views'])

        # Reload the object from the database to get the new view count
        obj.refresh_from_db()
        return obj

    # def get(self, request, *args, **kwargs):
    #     # Perform the increment before rendering the view
    #     art = self.get_object()
    #     Blogpost.objects.filter(pk=art.pk).update(number_of_views= art.number_of_views + 1)
    #     return super().get(request, *args, **kwargs)


class ArticleUpdateView(UpdateView):
    model = Blogpost
    fields = ['title', 'description']
    template_name = 'blog/article_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:article_details', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Blogpost
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:articles')


class ContactUsView(TemplateView):
    fields = ['name', 'email', 'message']
    template_name = 'blog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')
