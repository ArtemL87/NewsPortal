from django import template

register = template.Library()

word = ['объявил', 'закон', 'мир']

@register.filter()
def censor(values):
   for i in word:
      if i in values.lower():
         values = values.replace(i, f'{i[0]}{"*"*(len(i)-1)}')

   return f'{values}'