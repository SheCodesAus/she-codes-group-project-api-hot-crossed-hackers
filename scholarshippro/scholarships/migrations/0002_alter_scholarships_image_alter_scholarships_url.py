# Generated by Django 4.0.2 on 2022-08-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]