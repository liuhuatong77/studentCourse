# Generated by Django 3.0.4 on 2020-04-25 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48, verbose_name='班级姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.Account')),
                ('brief', models.TextField(verbose_name='简介')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='accounts',
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('a', '学生'), ('b', '老师'), ('c', '管理员')], default='a', max_length=1, verbose_name='身份'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.Account')),
                ('studentAddress', models.CharField(max_length=128, verbose_name='宿舍地址')),
                ('studentCredit', models.IntegerField(null=True, verbose_name='以修学分')),
                ('studentClasses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Classes')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='classesTeacher',
            field=models.ManyToManyField(to='account.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='courseStudent',
            field=models.ManyToManyField(to='account.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='courseTeacher',
            field=models.ManyToManyField(to='account.Teacher'),
        ),
    ]
