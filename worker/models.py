from django.db import models

from django.contrib.auth import get_user_model

from main.models import Indisturial_sector, Speciality, Currency_types

User = get_user_model()
 

class Worker(models.Model):
    """Nomzod"""

    GENDERS = (
        ('male', 'Erkak'),
        ('female', 'Ayol'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    full_name = models.CharField("FISH", max_length=100)
    gender = models.CharField('Jinsi', choices=GENDERS, max_length=10)
    birthday = models.DateField()
    industurial_sector_id = models.ForeignKey(Indisturial_sector, on_delete=models.CASCADE, verbose_name='Sanoat soha')
    specility_id = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Kasbi')
    salary = models.PositiveIntegerField('Maosh')
    currency_type_id = models.ForeignKey(Currency_types, on_delete=models.CASCADE)
    education = models.ManyToManyField('Education', blank=True)
    work_experience = models.ManyToManyField('Work_experience', blank=True)
    languages = models.ManyToManyField('Languages', blank=True)
    skills = models.ManyToManyField('Skills')
    driver_license = models.ManyToManyField('Driver_licenses', blank=True)
    is_freelancer = models.BooleanField('Frilans', default=False)

    class Meta:
        verbose_name = 'Nomzod'
        verbose_name_plural = 'Nomzodlar'


    def __str__(self): 
        return self.full_name

class Education(models.Model):
    """Ta'lim joyi"""
    global MONTHS
    MONTHS = (
        ('1', 'Yanvar'),
        ('2', 'Fevral'),
        ('3', 'Mart'),
        ('4', 'Aprel'),
        ('5', 'May'),
        ('6', 'Iyun'),
        ('7', 'Iyul'),
        ('8', 'Avgust'),
        ('9', 'Sentabr'),
        ('10', 'Oktabr'),
        ('11', 'Noyabr'),
        ('12', 'Dekabr'),
    )
    place_name  = models.CharField('Joy nomi', max_length=100)
    education_leval = models.ForeignKey('Education_level', on_delete=models.CASCADE)
    speciality = models.CharField("Mutaxassisligi", max_length=150)
    start_month = models.CharField('Boshlanish oyi', choices=MONTHS, max_length=15)
    start_year = models.PositiveIntegerField('Boshanish yili')
    is_active = models.BooleanField("Davom etmoqda", default=False)
    end_month = models.CharField('Tugash oyi', choices=MONTHS, max_length=15, null=True, blank=True)
    end_year = models.PositiveIntegerField('Tugash yili', null=True, blank=True)
    description = models.TextField('Tavsif', max_length=500)

    class Meta:
        verbose_name = 'Ta`lim joyi'
        verbose_name_plural = 'Ta`lim joylar'


    def __str__(self): 
        return f'{self.place_name} {self.education_leval}' 

class Education_level(models.Model):
    """Ta'lim darajasi"""
    name = models.CharField('Nomi', max_length=30)

    class Meta:
        verbose_name = 'Ta`lim darajasi'
        verbose_name_plural = 'Ta`lim darajalar'


    def __str__(self): 
        return self.name 


class Work_experience(models.Model):
    """Ish tajribasi"""
    position = models.CharField('Mansabi', max_length=100)
    company_name = models.CharField('Kompaniya nomi', max_length=100)
    start_month = models.CharField('Boshlanish oyi', choices=MONTHS, max_length=15)
    start_year = models.PositiveIntegerField('Boshanish yili')
    is_active = models.BooleanField("Davom etmoqda", default=False)
    end_month = models.CharField('Tugash oyi', choices=MONTHS, max_length=15, null=True, blank=True)
    end_year = models.PositiveIntegerField('Tugash yili', null=True, blank=True)
    description = models.TextField('Tavsif', max_length=500)

    class Meta:
        verbose_name = 'Ishlagan joyi'
        verbose_name_plural = 'Ishlagan joylari'


    def __str__(self): 
        return f'{self.company_name} da {self.position} bo`lib.' 

class Languages(models.Model):
    """Chet tili"""
    DARAJA = (
        ('a1', 'A1'),
        ('a2', 'A2'), 
        ('b1', 'B1'),
        ('b2', 'B2'), 
        ('c1', 'C1'),
        ('c2', 'C2'),
        ('-1', 'Ona tili') 
    )

    language_type = models.ForeignKey('Language_types', on_delete=models.CASCADE, verbose_name='Chet tili turi')
    level = models.CharField('Darajasi', choices=DARAJA, max_length=10)

    class Meta:
        verbose_name = 'Chet tili'
        verbose_name_plural = 'Chet tillari'


    def __str__(self): 
        return f'{self.language_type}  {self.level}' 

class Language_types(models.Model):
    """"Chet tili turlari"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Chet tili turi'
        verbose_name_plural = 'Chet tili turlari'


    def __str__(self): 
        return f'{self.name}' 


class Skills(models.Model):
    """Ko`nikmalar"""
    name = models.CharField('Nomi', max_length=100)

    class Meta:
        verbose_name = 'Ko`nikma'
        verbose_name_plural = 'Ko`nikmalar'


    def __str__(self): 
        return f'{self.name}' 


class Driver_licenses(models.Model):
    """Haydovchilik guvohnoma"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Haydovchilik guvohnoma'
        verbose_name_plural = 'Haydovchilik guvohnomalar'


    def __str__(self): 
        return f'{self.name}' 