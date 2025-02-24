from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(verbose_name="Titulo do Livro", max_length=255)
    author = models.CharField(verbose_name="Autor do Livro", max_length=255)
    description = models.TextField(verbose_name="Descrição do Livro", null=True, blank=True)
    instructions = models.CharField(verbose_name="Instruções", null=True, blank=True, max_length=255)
    cover = models.ImageField(verbose_name="Capa do Livro", upload_to="covers/")
    public_data = models.DateField(verbose_name="Data de Publicação", null=True, blank=True)
    category = models.ManyToManyField(verbose_name="Categoria do Livro", to=Category)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.author}")
        super().save(*args, **kwargs)

    @property
    def available(self):
        if self.rentals.filter(active=True):
            return False
        return True

    @property
    def rentais_list(self):
        return self.rentals.all().order_by("-pk")

    @property
    def short_desc(self):
        return f'{self.description[0:200]}...' if self.description else ''

    @property
    def who_rented(self):
        return self.rentals.get(active=True).user

    def __str__(self):
        return self.title
