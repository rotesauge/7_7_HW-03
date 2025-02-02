from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .filters import NewsFilter
from .forms import PostForm,ArticleForm
from django.views.generic import (ListView, DetailView, CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy,reverse


# Новости
#**************************************************************************

class PostList(ListView):
    #model = Post
    #ordering = 'datetime'

    queryset = Post.objects.filter(type = 'NW')
    template_name = 'News.html'
    context_object_name = 'news'
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

class PostDetail(DetailView):
    model = Post
    template_name = 'Post.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

    #def get_absolute_url(self):
    #    return reverse('post', args=[str(self.id)])
#**************************************************************************
def craate_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news/')
    form = PostForm()
    return render(request,'Post_Edit.html',{'form':form})
#**************************************************************************

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'Post_Edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NW'
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'Post_Edit.html'

# Представление удаляющее товар.
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

# Статьи
#*********************************************************************
#*********************************************************************


class ArticleList(ListView):
    #model = Post
    #ordering = 'datetime'

    queryset = Post.objects.filter(type='PO')
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

    #def get_absolute_url(self):
    #    return reverse('article', args=[str(self.id)])

class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'PO'
        return super().form_valid(form)

class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'

# Представление удаляющее товар.
class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')


