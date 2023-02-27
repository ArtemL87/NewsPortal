from django.shortcuts import render, reverse, redirect, get_object_or_404
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.core.mail import send_mail, EmailMultiAlternatives, mail_admins
from django.template.loader import render_to_string
from datetime import datetime
from .models import Post, Category
from .filters import PostFilter
from .forms import NewsForm, ArticleForm


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
        # if request.user in Category.subscribers.all():
        #     #получаем наш html
        #     html_content = render_to_string(
        #         'news_created.html',
        #         {
        #             'news':news,
        #         }
        #     )
        #     msg = EmailMultiAlternatives(
        #         subject=f'{news.title_news}',  # имя клиента и дата записи будут в теме для удобства
        #         body=f'{news.text_news}',  # сообщение с кратким описанием проблемы
        #         from_email='artem.l.1987@yandex.ru',
        #         # здесь указываете почту, с которой будете отправлять (об этом попозже)
        #         to = ['lordtemik@gmail.com', ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        #     )
        #     msg.attach_alternative(html_content, "text/html")
        #     msg.send()

        # отправляем письмо всем админам по аналогии с send_mail, только здесь получателя указывать не надо
        mail_admins(
            subject=f'{news.title_news}',
            message=news.text_news,
        )
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
        send_mail(
            subject=f'{article.title_news}',  # имя клиента и дата записи будут в теме для удобства
            message=f'{article.text_news}',  # сообщение с кратким описанием проблемы
            from_email='artem.l.1987@yandex.ru',
            # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=['lordtemik@gmail.com', ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )
        return super().form_valid(form)
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

class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category_com=self.category).order_by('-time_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subsriber'] = self.request.user not in self.category.subscribers.all()
        context['category_com'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})
# Create your views here.