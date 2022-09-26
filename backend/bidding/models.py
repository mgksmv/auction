from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from .tools import ResizeImageMixin


User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Item(ResizeImageMixin, models.Model):
    category = models.ForeignKey(
        to=Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
    )
    name = models.CharField('Название предмета', max_length=150)
    image = models.ImageField('Картинка', upload_to='item_images', default='item_images/default.png')
    description = models.TextField('Описание', max_length=300,null=True, blank=True)
    owner = models.ForeignKey(
        to=User,
        verbose_name='Владелец',
        related_name='owner',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    previous_owners = models.ManyToManyField(
        to=User,
        verbose_name='Бывшие владельцы',
        related_name='previous_owners',
        blank=True,
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'предмет на ставку'
        verbose_name_plural = 'Предметы на ставку'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.image:
            self.resize(self.image, (500, 500))
        super().save(*args, **kwargs)


class Wishlist(models.Model):
    item = models.ForeignKey(
        to=Item,
        verbose_name='Предмет',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'список желаемого'
        verbose_name_plural = 'Список желаемого'

    def __str__(self):
        return f'{self.item.name} - {self.user}'


class Auction(models.Model):
    item = models.ForeignKey(
        to=Item,
        verbose_name='Предмет',
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField('Цена', default=0)
    winning_price = models.PositiveIntegerField('Выигрышная цена', default=0, null=True, blank=True)
    starts_at = models.DateTimeField('Дата старта аукциона', default=timezone.now, editable=True)
    ends_at = models.DateTimeField('Дата окончания аукциона', default=timezone.now, editable=True)
    winner = models.ForeignKey(
        to=User,
        verbose_name='Победитель',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    is_finished = models.BooleanField('Завершён?', default=False)

    class Meta:
        verbose_name = 'аукцион'
        verbose_name_plural = 'Аукционы'

    def __str__(self):
        return str(self.item)


class Bid(models.Model):
    auction = models.ForeignKey(
        to=Auction,
        verbose_name='Аукцион',
        related_name='bids',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField('Цена', default=0)
    bid_placed_at = models.DateTimeField('Дата ставки', default=timezone.now)

    class Meta:
        verbose_name = 'ставка'
        verbose_name_plural = 'Ставки'

    def __str__(self):
        return f'{self.auction} / {self.user} / {self.price}'
