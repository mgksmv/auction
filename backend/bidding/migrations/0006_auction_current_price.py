# Generated by Django 4.1.1 on 2022-09-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0005_alter_bid_bid_placed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='current_price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Текущая цена'),
        ),
    ]
