# Generated by Django 2.1.5 on 2019-08-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maestros', '0002_auto_20190803_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestros',
            name='cedulaprofesional',
            field=models.CharField(max_length=150),
        ),
    ]
