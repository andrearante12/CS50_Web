# Generated by Django 4.0.4 on 2022-04-16 05:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_userprofile_description_userprofile_followers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 5, 39, 30, 762778, tzinfo=utc)),
        ),
    ]
