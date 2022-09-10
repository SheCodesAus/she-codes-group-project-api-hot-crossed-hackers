from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUser(AbstractUser):
    post_code = models.IntegerField(default=4000)
    year_of_birth = models.IntegerField(default=1990)
    class Gender(models.TextChoices):
        ANY = 'AN', _('Any')
        FEMALE = 'FE', _('Female')
        MALE = 'MA', _('Male')
        NONBINARY = 'NB', _('Non-Binary')

    gender = models.CharField (
        max_length=2,
        choices = Gender.choices,
        default=Gender.ANY
    )

    class IndigenousStatus(models.TextChoices):
        ANY = 'AN', _('Any')
        ABORIGINAL = 'AB', _('Aboriginal')
        ATSI = 'AT', _('Aboriginal Torres Strait Islander')
        NOT = 'NB', _('Not ATSI')

    indigenous_status = models.CharField (
        max_length=2,
        choices = IndigenousStatus.choices,
        default=IndigenousStatus.ANY 
    )

    class VisionImpairment(models.TextChoices):
        ANY = 'AN', _('Any')
        YES = 'YE', _('Yes')
        NO = 'NO', _('No')

    vision_impairment = models.CharField (
        max_length=2,
        choices = VisionImpairment.choices,
        default=VisionImpairment.ANY 
    )

    class LowIncome(models.TextChoices):
        ANY = 'AN', _('Any')
        YES = 'YE', _('Yes')
        NO = 'NO', _('No')

    low_income = models.CharField (
        max_length=2,
        choices = LowIncome.choices,
        default=LowIncome.ANY 
    )

    class ESOL(models.TextChoices):
        ANY = 'AN', _('Any')
        YES = 'YE', _('Yes')
        NO = 'NO', _('No')

    esol = models.CharField (
        max_length=2,
        choices = ESOL.choices,
        default=ESOL.ANY 
    )

    class Duration(models.TextChoices):
        ANY = 'AN', _('Any')
        WORKSHOP = 'WO', _('Workshop')
        BOOTCAMP = 'BO', _('Boot Camp')
        UNDERGRAD = 'UG', _('Undergraduate')

    duration = models.CharField (
        max_length=2,
        choices = Duration.choices,
        default=Duration.ANY 
    )
    class Education(models.TextChoices):
        ANY = 'AN', _('Any')
        HIGHSCHOOL = 'HI', _('Highschool')
        DIPLOMA = 'DI', _('Diploma')
        BACHELOR = 'BA', _('Bachelor')
        POST_GRAD = 'PO', _('Post_Grad')
        TECHNICAL_COLLEGE = 'TE', _('Technical_College')

    education = models.CharField (
        max_length=2,
        choices = Education.choices,
        default=Education.ANY 
    )

    class Employment(models.TextChoices):
        ANY = 'AN', _('Any')
        UNEMPLOYED = 'UN', _('Unemployed')
        PART_TIME = 'PA', _('Part_Time')
        FULL_TIME = 'FU', _('Full_Time')
        CASUAL = 'CA', _('Casual')

    employment = models.CharField (
        max_length=2,
        choices = Employment.choices,
        default=Employment.ANY 
    )   

    class Industry(models.TextChoices):
        ANY = 'AN', _('Any')
        FINANCE = 'FI', _('Finance')
        CONSTRUCTION = 'CO', _('Construction')
        EDUCATION = 'ED', _('Education')
        FARMING_AND_ANIMALS = 'FA', _('Farming_and_Animals')
        HEALTHCARE_AND_MEDICAL = 'HE', _('Healthcare_and_Medical')
        HOSPITALITY_AND_TOURISM = 'HO', _('Hospitality_and_Tourism')
        ICT = 'IC', _('ICT')
        LEGAL = 'LE', _('Legal')
        REALESTATE = 'RE', _('Real_estate')
        TRANSPORT = 'TR', _('Transport')
        SERVICES_AND_TRADES = 'SE', _('Services_and_Trades')

    industry = models.CharField (
        max_length=2,
        choices = Industry.choices,
        default=Industry.ANY 
    )   


    def _str_(self):
        return self.username
