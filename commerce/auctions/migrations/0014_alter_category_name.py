# Generated by Django 4.0.3 on 2022-03-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_remove_comment_auction_remove_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home and Decor', 'Home and Decor'), ('Toys and Games', 'Entertainment')], default='Misc', max_length=64),
        ),
    ]