# Generated by Django 3.0.2 on 2020-01-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20200122_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(max_length=254, null=True)),
                ('total', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='foodpair',
            name='food',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='foodpair',
            name='qty',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='foodpair',
            name='ordername',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.order'),
        ),
    ]