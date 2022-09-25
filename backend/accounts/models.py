from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.functional import cached_property
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', max_length=32, unique=True)
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    birthday = models.DateField('День рождения', blank=True, null=True)
    photo = models.ImageField('Фотография', blank=True, null=True, default='profile_pic_default.jpg')
    phone = models.CharField(
        'Телефон',
        max_length=15,
        validators=[RegexValidator(r'^\+?\d{8,15}$')],
        blank=True,
        null=True
    )

    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    last_login = models.DateTimeField('Последний вход', auto_now_add=True)
    is_active = models.BooleanField('Активный', default=False)
    is_admin = models.BooleanField('Админ', default=False)
    is_staff = models.BooleanField('Статус персонала', default=False)
    is_superuser = models.BooleanField('Статус суперпользователя', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        if not self.first_name or not self.last_name:
            return f'{self.email}'
        return f'{self.first_name} {self.last_name}'

    @cached_property
    def get_full_name(self):
        return str(self)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        instance.is_active = True
        instance.save()
        Token.objects.create(user=instance)
