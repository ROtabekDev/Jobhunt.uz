from django.db import models

from django.contrib.auth import get_user_model

from main.models import Indisturial_sector, Speciality, Currency_types, Region, District

User = get_user_model()

class Company(models.Model):
    """Kompaniya"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    name_company = models.CharField('Kompaniya nomi', max_length=100)
    legal_name_company = models.CharField('Kompaniyaninhg yuridik nomi', max_length=100)
    industrial_sector = models.ManyToManyField(Indisturial_sector)
    speciality = models.ManyToManyField(Speciality)
    size_company = models.ForeignKey('Size_company', on_delete=models.CASCADE, verbose_name='Hodimlar soni')
    type_company = models.ForeignKey('Type_company', on_delete=models.CASCADE, verbose_name='Kompaniya turi')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, verbose_name='Bo`sh ish o`rni')
    description = models.TextField('Tavsif', max_length=500)
    web_page = models.CharField('Web sahifa', max_length=100)


    class Meta:
        verbose_name = 'Kompaniya'
        verbose_name_plural = 'Kompaniyalar'


    def __str__(self): 
        return f'{self.user} {self.name_company}' 

class Size_company(models.Model):
    """Kompaniya hajmi"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Kompaniya hajmi'
        verbose_name_plural = 'Kompaniya hajmi'


    def __str__(self): 
        return self.name 

class Type_company(models.Model):
    """Kompaniya turi"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Kompaniya turi'
        verbose_name_plural = 'Kompaniya turi'


    def __str__(self): 
        return self.name 


class Vacancy(models.Model):
    """Bo`sh ish o`rni"""
    SALARY_TYPE = (
        ('1', 'Naqd'),
        ('0', 'Suhbat orqali'),
    )

    industrial_sector = models.ForeignKey(Indisturial_sector, on_delete=models.CASCADE, verbose_name='Sanoat sohasi')
    title = models.CharField('Vakansiya nomi', max_length=100)
    work_experience = models.ForeignKey('Experience_for_vacany', on_delete=models.CASCADE, verbose_name='Tajriba')
    type_work = models.ForeignKey('Work_types', on_delete=models.CASCADE, verbose_name='Ish turi')
    salary_type = models.CharField('Maosh turi', choices=SALARY_TYPE, max_length=20)
    currency_type = models.ForeignKey(Currency_types, on_delete=models.CASCADE, verbose_name='Pul birligi')
    start_salary = models.PositiveIntegerField('Boshlang`ich maosh')
    end_salary = models.PositiveIntegerField('Oxirgi maosh')
    is_online = models.BooleanField('Online')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Viloyat')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Tuman')
    requirements = models.ManyToManyField('Requirements', verbose_name='Talablar')
    tasks = models.ManyToManyField('Tasks', verbose_name='Vazifalar')
    conditions = models.ManyToManyField('Conditions', verbose_name='Shartlar')
    tags = models.ManyToManyField('Tags', verbose_name='Teglar')
    updated = models.DateTimeField('O`zgartirildi', auto_now=True)
    created = models.DateTimeField('Yaratildi', auto_now_add=True)


    class Meta:
        verbose_name = 'Bo`sh ish o`rni'
        verbose_name_plural = 'Bo`sh ish o`rinlari'


    def __str__(self): 
        return f'{self.industrial_sector} {self.title}' 


class Experience_for_vacany(models.Model):
    """Ish tajribasi vakansiya uchun"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Ish tajribasi'
        verbose_name_plural = 'Ish tajribasi'


    def __str__(self): 
        return self.name 

class Work_types(models.Model):
    """Ish turi"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Ish turi'
        verbose_name_plural = 'Ish turlari'


    def __str__(self): 
        return self.name 


class Requirements(models.Model):
    """Talablar"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Talab'
        verbose_name_plural = 'Talablar'


    def __str__(self): 
        return self.name 

class Tasks(models.Model):
    """Vazifalar"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Vazifa'
        verbose_name_plural = 'Vazifalar'


    def __str__(self): 
        return self.name 

class Conditions(models.Model):
    """Shartlar"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Shart'
        verbose_name_plural = 'Shartlar'


    def __str__(self): 
        return self.name 


class Tags(models.Model):
    """Teglar"""
    name = models.CharField('Nomi', max_length=50)

    class Meta:
        verbose_name = 'Teglar'
        verbose_name_plural = 'Teglar'


    def __str__(self): 
        return self.name 


