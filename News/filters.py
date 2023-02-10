from django_filters import \
    (FilterSet, ModelChoiceFilter)
from .models import Post, User


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author__user_com',
        queryset=User.objects.all(),
        label='Author',
    )

    class Meta:
       model = Post
       fields = {
           # поиск по названию
           'title_news': ['icontains'],
           # позже указываемой даты
           'time_in': ['gt'],
       }