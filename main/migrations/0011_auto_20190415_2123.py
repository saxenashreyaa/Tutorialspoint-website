# Generated by Django 2.1.7 on 2019-04-15 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190415_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 21, 23, 26, 419415), verbose_name='date published'),
        ),
    ]
