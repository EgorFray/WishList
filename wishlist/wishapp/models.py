from django.db import models
from django.utils.text import slugify

# Create your models here.


class Goods(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.CharField(max_length=1000, null=False, blank=False)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Goods, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class WishList(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Goods)

