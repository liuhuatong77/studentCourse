'''
@Author: your name
@Date: 2020-04-08 22:04:59
@LastEditTime: 2020-04-08 22:05:16
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /studentCourse/account/models.py
'''
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    TYPE = (
        ('a','学生'),
        ('b','老师'),
        ('c','管理员')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    status = models.CharField(choices=TYPE, verbose_name='身份', max_length=1,default='a')
    code = models.CharField( verbose_name='学号/工号',max_length=24,unique=True)
    telephone = models.CharField(verbose_name='手机号',max_length=11,null=True,unique=True)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return "{}".format(self.user.__str__())
class Student(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    studentAddress = models.CharField(max_length=128, verbose_name="宿舍地址",null=True)
    studentCredit = models.IntegerField(null=True, verbose_name="已修学分")
    studentClasses = models.ForeignKey("Classes",on_delete=models.CASCADE,verbose_name="班级",null=True)  # 与班级多对一
    class Meta:
        verbose_name="学生"
        verbose_name_plural=verbose_name


class Teacher(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    brief = models.TextField(verbose_name="简介",null=True)

    class Meta:
        verbose_name="老师"
        verbose_name_plural=verbose_name
class Admin(models.Model):
    id = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        verbose_name="管理员"
        verbose_name_plural=verbose_name
class Course(models.Model):
    TYPE = (
        ('a','必修'),
        ('b','选修')
    )
    name = models.CharField(max_length=50, verbose_name="课程名称",unique=True)
    credit = models.CharField(max_length=4,verbose_name="学分")
    type = models.CharField(choices=TYPE, verbose_name='必修/选修', max_length=1, default='a')
    code = models.CharField(max_length=24,verbose_name="课程编号",unique=True)
    courseStudent = models.ManyToManyField(Student,verbose_name="课程学生")
    courseTeacher = models.ManyToManyField(Teacher,verbose_name="课程老师")


    class Meta:
        verbose_name="课程"
        verbose_name_plural=verbose_name

class Classes(models.Model):
    name = models.CharField(max_length=48, verbose_name="班级姓名",unique=True)
    classesTeacher = models.ManyToManyField(Teacher)
    classesCourse = models.ManyToManyField(Course)

    class Meta:
        verbose_name="班级"
        verbose_name_plural=verbose_name




