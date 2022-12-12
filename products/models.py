from django.contrib.postgres.fields import ArrayField
from django.db import models


PRODUCT_STATUS_CHOICES = [
    ('InStock', 'В наличии'),
    ('UnderTheOrder', 'Под заказ'),
    ('ExpectedReceipt', 'Ожидается поступление'),
    ('OutOfStock', 'Нет в наличии'),
    ('NotProduced', 'Не производится'),
]


class Image(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/', max_length=255)
    formats = ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    article = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS_CHOICES)
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, blank=True, null=True)
