# Generated by Django 2.2.7 on 2020-12-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchens', '0002_auto_20201220_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='daily_order_count',
            field=models.IntegerField(default=0),
        ),
    ]
