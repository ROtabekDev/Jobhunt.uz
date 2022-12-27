import uuid
from django.db import models

from django.contrib.auth.hashers import make_password

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):
    """Maxsus foydalanuvchi menejeri"""
    def create_user(self, phone_number, email, password=None):  
        user = self.model( 
            phone_number=phone_number,
            email=email  
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, email, password=None): 
        user = self.model(phone_number=phone_number, email=email, password=make_password(password)) 
        user.is_superuser = True  
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Foydalanuvchilar""" 
    phone_number = models.CharField(
        "Telefon nomer", 
        max_length=15, 
        unique=True,
        error_messages={'unique': 'Bu telefon nomer ro`yhatdan o`tgan!'},
        validators=[RegexValidator(regex='^[+][998]{3}?[0-9]{9}$', message='Iltimos telefon nomerni to`g`ri kiriting')]
        )
    email = models.EmailField('Elektron pochta')
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name="Viloyat yoki shahari", null=True, blank=True)
    district_id = models.ForeignKey('District', on_delete=models.CASCADE, verbose_name="Tumani", null=True, blank=True)
    social_networs = models.ManyToManyField('Social_networks', verbose_name="Ijtimoiy tarmoqlari") 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 

 
    USERNAME_FIELD = 'phone_number' 
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Barcha foydalanuvchilar'

    def __str__(self): 
        return self.phone_number


    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class Region(models.Model):
    """Viloyat va shaharlar"""
    name = models.CharField("Nomi", max_length=50)

    class Meta:
        verbose_name = 'Viloyat yoki shahar'
        verbose_name_plural = 'Viloyat va shaharlar'

    def __str__(self): 
        return self.name

class District(models.Model):
    """Tumanlar"""
    name = models.CharField("Nomi", max_length=50)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Viloyat yoki shahar nomi')

    class Meta:
        verbose_name = 'Tuman'
        verbose_name_plural = 'Tumanlar'

    def __str__(self): 
        return self.name

class Social_networks(models.Model):
    """Ijtiomiy tarmoqlar"""
    social_network_id = models.ForeignKey('Social_network_types', on_delete=models.CASCADE, verbose_name='Ijtimoiy tarmoq')
    nickname = models.CharField("Foydalanuvchi nomi", max_length=50)

    class Meta:
        verbose_name = 'Ijtimoiy tarmoq'
        verbose_name_plural = 'Ijtimoiy tarmoqlar'

    def __str__(self): 
        return self.name

class Social_network_types(models.Model):
    """Ijtiomiy tarmoq turlari"""
    name = models.CharField("Nomi", max_length=50)

    class Meta:
        verbose_name = 'Ijtimoiy tarmoq'
        verbose_name_plural = 'Ijtimoiy tarmoqlar'

    def __str__(self): 
        return self.name

class Indisturial_sector(models.Model):
    """Sanoat sohasi"""
    name = models.CharField("Nomi", max_length=50)
    
    class Meta:
        verbose_name = 'Sanoat soha'
        verbose_name_plural = 'Sanoat sohalar'

    def __str__(self): 
        return self.name

class Speciality(models.Model):
    """Mutaxassislik"""
    name = models.CharField("Nomi", max_length=50)
    idustrial_sector_id = models.ForeignKey(Indisturial_sector, on_delete=models.CASCADE, verbose_name='Sanoat soha')
    for_worker = models.BooleanField("Ishchi uchun")
    
    class Meta:
        verbose_name = 'Mutaxassislik'
        verbose_name_plural = 'Mutaxassisliklar'

    def __str__(self): 
        return self.name

class Currency_types(models.Model):
    """Pul birliklari"""
    name = models.CharField("Nomi", max_length=50)

    class Meta:
        verbose_name = 'Pul birligi'
        verbose_name_plural = 'Pul birliklari'

    def __str__(self): 
        return self.name