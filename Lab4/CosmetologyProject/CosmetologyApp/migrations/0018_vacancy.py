# Generated by Django 4.1.9 on 2023-09-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmetologyApp', '0017_alter_service_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_character', models.CharField(help_text='enter job character', max_length=50)),
                ('experience', models.CharField(help_text='enter experience', max_length=50)),
                ('description', models.TextField(help_text='enter vacancy description')),
                ('salary', models.CharField(help_text='enter salary', max_length=50)),
            ],
        ),
    ]
