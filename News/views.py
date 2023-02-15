from django.shortcuts import render
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, View
from .models import Post
from .filters import PostFilter
from .forms import NewsForm, ArticleForm, NewsDeleteForm, ArticleDeleteForm


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-time_in'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10 # количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'


# представление для создания новости
class NewsCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.news_article = 'новость'
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')


# представление для изменения новости
@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class NewsUpdate(UpdateView, PermissionRequiredMixin):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'
    def form_valid(self, form):
        news = form.save(commit=False)
        if news.news_article == 'новость':
            return super().form_valid(form)
    success_url = reverse_lazy('post_list')


# Представление удаляющее новости
class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    def form_valid(self, form):
        if 'news/' in self.request.path and self.object.news_article == 'новость':
            return super().form_valid(form)
    success_url = reverse_lazy('post_list')


# представление для создания статьи
class ArticleCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_post',)
    form_class = ArticleForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.news_article = 'статья'
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')


# представление для изменения статьи
@method_decorator(login_required(login_url = '/accounts/login/'), name='dispatch')
class ArticleUpdate(UpdateView, PermissionRequiredMixin):
    permission_required = ('news.change_post',)
    form_class = ArticleForm
    model = Post
    template_name = 'post_edit.html'
    def form_valid(self, form):
        article = form.save(commit=False)
        if article.news_article == 'статья':
            return super().form_valid(form)
    success_url = reverse_lazy('post_list')


# Представление удаляющее статьи
class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    def form_valid(self, form):
        # article = form.save(commit=False)
        if 'articles/' in self.request.path and self.object.news_article == 'статья':
            return super().form_valid(form)
        return render(request)
    success_url = reverse_lazy('post_list')



# # Create your views here.
