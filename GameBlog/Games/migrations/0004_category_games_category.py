# Generated by Django 5.0.1 on 2024-01-10 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0003_alter_games_options_alter_games_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Жанр')),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Games.category', verbose_name='Жанр'),
        ),
    ]
