# Generated by Django 2.2.6 on 2020-01-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200116_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='fnum',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
