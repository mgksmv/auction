# Generated by Django 4.1.1 on 2022-09-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auction_winner_alter_bid_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_placed_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата ставки'),
        ),
    ]