# Generated by Django 2.2.6 on 2020-01-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200122_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tot',
            field=models.IntegerField(default=0),
        ),
    ]