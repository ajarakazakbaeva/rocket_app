from django.contrib.auth.models import User
from django.db import models

from rocket_application.couriers.models import Courier
from rocket_application.profiles.models import Customer

Status_choices = (
    ('not shipped', 'не доставлено'),
    ('shipped', 'доставлено')
)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
    related_name='products',
    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, related_name='orders', on_delete=models.CASCADE)
    pickup_location = models.CharField(db_index=True, max_length=255)
    destination = models.CharField(db_index=True, max_length=255)
    weight = models.IntegerField(db_index=True)
    status = models.CharField(max_length=255,choices=Status_choices, default='не доставлено')
    order_item = models.ManyToManyField(Product)
