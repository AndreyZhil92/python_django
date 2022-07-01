from django.db import models

class Artiles(models.Models):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Anonc', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DataTimeField('Дата публикации')

    def __str__(self):
        return self.title