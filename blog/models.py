from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    number_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} {self.description} {self.is_published}'


    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['title']
