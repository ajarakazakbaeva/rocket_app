from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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
    customer = models.ForeignKey('profiles.Customer', related_name='customer_orders', on_delete=models.CASCADE, default='1', blank=True)
    courier = models.ForeignKey('couriers.Courier', related_name='courier_orders', on_delete=models.CASCADE, default='1', blank=True)
    destination = models.CharField(db_index=True, max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    requested_delivery_date = models.DateTimeField(blank=True, null=True)
    weight = models.IntegerField(db_index=True)
    status = models.CharField(max_length=255,choices=Status_choices, default='не доставлено')
    # order_item = models.ManyToManyField(Product, blank=True, default='1')

    def __str__(self):
        return str(self.id)
