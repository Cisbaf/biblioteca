from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField("Nome da Categoria", max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField("Título do Livro", max_length=255)
    author = models.CharField("Autor do Livro", max_length=255)
    description = models.TextField("Descrição do Livro", null=True, blank=True)
    instructions = models.CharField("Instruções", null=True, blank=True, max_length=255)
    cover = models.ImageField("Capa do Livro", upload_to="covers/")
    public_data = models.DateField("Data de Publicação", null=True, blank=True)
    category = models.ManyToManyField(verbose_name="Categoria do Livro", to=Category)
    slug = models.SlugField("Apelido", max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

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
