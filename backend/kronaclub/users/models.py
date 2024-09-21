from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, first_name, date_of_birth, password=None):
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            first_name=first_name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='e-mail', unique=True)
    # first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name='birth date', null=True, blank=True)
    telegram_login = models.CharField(max_length=30, null=True, blank=True)
    telegram_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'date_of_birth', 'last_name']

    objects = CustomUserManager()
  
    def __str__(self):
        return f'{self.id}. {self.first_name} - {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class TypeOfUser(models.Model):
    name = models.CharField(verbose_name='Тип пользователя', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователей'
    

class UserType(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='user_type')
    type_of_user = models.ForeignKey(TypeOfUser, on_delete=models.CASCADE, null=True, related_name='user_type')

    def __str__(self):
        return f'{self.user.id}. {self.user.first_name} - {self.type_of_user.name}' 

    class Meta:
        verbose_name = 'Связь пользователя и типа пользователя'
        verbose_name_plural = 'Связи пользователей и типов пользователей'
