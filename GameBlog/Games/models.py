from django.db import models
from django.urls import reverse_lazy


class Games(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Жанр')

    def get_absolute_url(self):
        return reverse_lazy('View_games', kwargs={'games_id': self.pk})

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created_at']

class Users(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    adress = models.CharField(max_length=150, verbose_name='Адрес')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    photo = models.ImageField(upload_to='media/users/', verbose_name='Фото')

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Жанр')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'
        ordering = ['title']