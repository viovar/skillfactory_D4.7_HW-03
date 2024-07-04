
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm, ArticleForm
from .models import Post





# Create your views here.

class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'flatpages/news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by(
        '-dateCreation'
    )
    paginate_by=2


class NewDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'post_search.html'
    context_object_name = 'search'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset']=self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create_news.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/create/':
            post.categoryType = 'NW'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text', 'categories']

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/<int:pk>/edit/':
            post.categoryType = 'NW'
        post.save()
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list') #This redirects to the home page after deleting a post

    def get_template_names(self):
        post = self.get_object()
        if post.categoryType == 'AR':
            return ['articles_delete.html']
        elif post.categoryType == 'NW':
            return ['post_delete.html']
        else:
            pass
