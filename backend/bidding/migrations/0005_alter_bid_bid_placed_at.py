# Generated by Django 4.1.1 on 2022-09-25 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0004_alter_bid_bid_placed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_placed_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата ставки'),
        ),
    ]
