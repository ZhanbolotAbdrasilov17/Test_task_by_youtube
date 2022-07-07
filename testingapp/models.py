from django.db import models

# Create your models here.

class Category(models.Model):
    categot_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.category_name

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Новости")
    text = models.TextField("Описание")
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="news")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ['title']

