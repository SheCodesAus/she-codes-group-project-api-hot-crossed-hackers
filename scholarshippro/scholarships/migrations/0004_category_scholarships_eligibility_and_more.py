# Generated by Django 4.0.2 on 2022-09-04 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0003_scholarships_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='scholarships',
            name='eligibility',
            field=models.TextField(default='No Eligibility Criteria Recorded', max_length=800),
        ),
        migrations.AddField(
            model_name='scholarships',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scholarship_id', to='scholarships.category'),
        ),
    ]