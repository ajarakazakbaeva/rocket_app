# Generated by Django 4.0.4 on 2022-05-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0007_remove_order_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='requested_delivery_date',
            field=models.DateTimeField(blank=True, default='2023-01-01', null=True),
        ),
    ]