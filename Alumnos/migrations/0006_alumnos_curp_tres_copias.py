# Generated by Django 2.1.5 on 2019-09-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumnos', '0005_auto_20190814_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='curp_tres_copias',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]