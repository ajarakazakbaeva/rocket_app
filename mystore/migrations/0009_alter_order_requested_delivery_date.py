# Generated by Django 4.0.4 on 2022-05-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0008_order_requested_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requested_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
