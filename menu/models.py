from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория блюд"
        verbose_name_plural = "Категории блюды"

    def __str__(self):
        return self.name


# class SubCategory(models.Model):
#     name = models.CharField("Название блюда", max_length=50)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
#     slug = models.SlugField(max_length=50, unique=True)
#
#     class Meta:
#         verbose_name = "Название категори"
#         verbose_name_plural = "Название категории"
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Название блюда", max_length=200)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to="products/images/")
    is_active = models.BooleanField("Активный", default=True)

    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Название"
        verbose_name_plural = "Название блюд"

    def __str__(self):
        return self.name
