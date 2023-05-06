from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='media/projects/',
        verbose_name='Изображение'
    )
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.title


class Appeal(models.Model):
    name = models.CharField(max_length=50, verbose_name='Автор')
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Обращение')

    def __str__(self):
        return self.name
