# Generated by Django 3.0.4 on 2020-04-28 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200425_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': '管理员', 'verbose_name_plural': '管理员'},
        ),
        migrations.AlterModelOptions(
            name='classes',
            options={'verbose_name': '班级', 'verbose_name_plural': '班级'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程', 'verbose_name_plural': '课程'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '老师', 'verbose_name_plural': '老师'},
        ),
        migrations.AddField(
            model_name='classes',
            name='classesCourse',
            field=models.ManyToManyField(to='account.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseStudent',
            field=models.ManyToManyField(to='account.Student', verbose_name='课程学生'),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseTeacher',
            field=models.ManyToManyField(to='account.Teacher', verbose_name='课程老师'),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('a', '必修'), ('b', '选修')], default='a', max_length=1, verbose_name='必修/选修'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentClasses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Classes', verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentCredit',
            field=models.IntegerField(null=True, verbose_name='已修学分'),
        ),
    ]
