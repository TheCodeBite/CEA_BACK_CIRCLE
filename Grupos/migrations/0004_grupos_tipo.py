# Generated by Django 2.1.5 on 2019-08-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupos', '0003_remove_grupos_modalidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupos',
            name='tipo',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
