# Generated by Django 3.0.4 on 2020-04-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200413_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='telephone',
            field=models.CharField(default=0, max_length=11, verbose_name='手机号'),
            preserve_default=False,
        ),
    ]
