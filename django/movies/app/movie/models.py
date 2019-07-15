from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'