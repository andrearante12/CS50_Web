# Generated by Django 4.0.3 on 2022-04-19 04:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 4, 18, 59, 406699, tzinfo=utc)),
        ),
    ]
