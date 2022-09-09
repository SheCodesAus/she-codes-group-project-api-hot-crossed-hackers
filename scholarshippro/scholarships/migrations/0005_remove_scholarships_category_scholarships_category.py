# Generated by Django 4.0.2 on 2022-09-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0004_category_scholarships_eligibility_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarships',
            name='category',
        ),
        migrations.AddField(
            model_name='scholarships',
            name='category',
            field=models.ManyToManyField(to='scholarships.Category'),
        ),
    ]
