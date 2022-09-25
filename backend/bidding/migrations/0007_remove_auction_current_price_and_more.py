# Generated by Django 4.1.1 on 2022-09-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0006_auction_current_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='current_price',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='starting_price',
        ),
        migrations.AddField(
            model_name='auction',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
    ]
