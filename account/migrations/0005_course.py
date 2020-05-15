# Generated by Django 3.0.4 on 2020-04-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('credit', models.CharField(max_length=4, verbose_name='学分')),
                ('type', models.CharField(choices=[('a', '必修'), ('b', '选修')], default='a', max_length=1, verbose_name='选修/必修')),
                ('code', models.CharField(max_length=24, verbose_name='课程编号')),
                ('accounts', models.ManyToManyField(to='account.Account')),
            ],
        ),
    ]