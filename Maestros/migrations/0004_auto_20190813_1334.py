# Generated by Django 2.1.5 on 2019-08-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maestros', '0003_auto_20190813_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestros',
            name='cedulaprofesional',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
