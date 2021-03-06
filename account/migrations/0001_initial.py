# Generated by Django 3.0.4 on 2020-04-11 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('a', '学生'), ('b', '老师')], default='a', max_length=1, verbose_name='身份')),
                ('code', models.IntegerField(max_length=24, verbose_name='学号/工号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'users',
            },
        ),
    ]
