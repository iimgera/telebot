# Generated by Django 4.2 on 2023-05-03 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Автор')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Обращение')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='works/%Y/%m/%d/', verbose_name='Изображение')),
                ('link', models.URLField(verbose_name='Ссылка')),
            ],
        ),
    ]