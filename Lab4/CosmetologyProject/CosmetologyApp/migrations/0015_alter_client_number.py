# Generated by Django 4.1.9 on 2023-06-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosmetologyApp', '0014_client_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.CharField(help_text='+375 (29) xxx-xx-xx', max_length=20),
        ),
    ]
