# Generated by Django 4.0.2 on 2022-09-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_duration_customuser_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='employment',
            field=models.CharField(choices=[('AN', 'Any'), ('UN', 'Unemployed'), ('PA', 'Part_Time'), ('FU', 'Full_Time'), ('CA', 'Casual')], default='AN', max_length=2),
        ),
        migrations.AddField(
            model_name='customuser',
            name='industry',
            field=models.CharField(choices=[('AN', 'Any'), ('FI', 'Finance'), ('CO', 'Construction'), ('ED', 'Education'), ('FA', 'Farming_and_Animals'), ('HE', 'Healthcare_and_Medical'), ('HO', 'Hospitality_and_Tourism'), ('IC', 'ICT'), ('LE', 'Legal'), ('RE', 'Real_estate'), ('TR', 'Transport'), ('SE', 'Services_and_Trades')], default='AN', max_length=2),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='duration',
            field=models.CharField(choices=[('AN', 'Any'), ('WO', 'Workshop'), ('BO', 'Boot Camp'), ('UG', 'Undergraduate')], default='AN', max_length=2),
        ),
    ]
