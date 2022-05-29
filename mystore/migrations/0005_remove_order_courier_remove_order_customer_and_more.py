# Generated by Django 4.0.4 on 2022-05-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0004_alter_order_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='courier',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_item',
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.IntegerField(db_index=True),
        ),
    ]