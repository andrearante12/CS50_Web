# Generated by Django 4.0.3 on 2022-03-24 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_auction_listings_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.AddField(
            model_name='auction_listings',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='auction_category', to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='auction_listings',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_who_created_item', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Misc', max_length=64),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]