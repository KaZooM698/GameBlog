# Generated by Django 5.0.1 on 2024-01-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0002_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ['-created_at'], 'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterField(
            model_name='games',
            name='content',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='games',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='games',
            name='photo',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='games',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='games',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='users',
            name='adress',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(upload_to='media/users/', verbose_name='Фото'),
        ),
    ]
