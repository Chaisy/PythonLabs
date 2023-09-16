# Generated by Django 4.1.9 on 2023-09-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CosmetologyApp', '0026_alter_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_in_shedule', to='CosmetologyApp.doctor'),
        ),
    ]
