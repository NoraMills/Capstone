# Generated by Django 3.2.7 on 2021-09-20 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 20, 14, 4, 16, 274807, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
