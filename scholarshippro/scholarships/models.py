from ast import FormattedValue
from nntplib import NNTP_PORT
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Scholarships(models.Model):
    title = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    description = models.TextField()
    eligibility = models.TextField(max_length=800, default='No Eligibility Criteria Recorded')
    url = models.CharField(max_length=200)
    closing_date = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_scholarships'
    )
    favorites = models.ManyToManyField(get_user_model(), related_name='scholarship_favorite', blank=True)

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