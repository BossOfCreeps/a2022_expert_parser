# Generated by Django 4.0.5 on 2022-06-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='link',
            field=models.URLField(default='', verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
