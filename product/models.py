from django.db import models

from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='color')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    product_price = models.ForeignKey("product.Price", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True)


class Price(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='prices')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='prices')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.title + ' ' + self.size.title + ' ' + self.color.title