# Generated by Django 2.1.7 on 2019-03-29 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190329_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 16, 7, 51, 150184), verbose_name='date published'),
        ),
    ]
