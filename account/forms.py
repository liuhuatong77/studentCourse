from captcha.fields import CaptchaField
from django import forms
# Create your views here.
from django.contrib.auth.models import User
from django.forms import widgets

from account.models import Course, Account, Classes


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.CharField(label="code",max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    status=forms.CharField(
            initial='a',
            widget=widgets.Select(choices=(('a','学生'),('b','老师'),('c','管理员')),attrs={'class': 'btn btn-default'})
                )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("your username must be at least 3 characters log")
        elif len(username) > 20:
            raise forms.ValidationError("your username is too long")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('your username already exists')
        return username
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch Please enter again')

        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label='验证码')
    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError('This username does not exist Please register first')
        else:
            return username

# class ProfileUpdateForm(forms.Form):
#     username = forms.CharField(label='username',max_length=24)
#     status = forms.CharField(
#         initial='a',
#         widget=widgets.Select(choices=(('a', '学生'), ('b', '老师'),),attrs={'class': 'btn btn-default'})
#     )
#     code = forms.CharField(label='学号/工号',max_length=24)
#     telephone = forms.CharField(label='Telephone', max_length=13, required=False)

class ProfileStudentForm(forms.Form):   #更新学生信息
    studentAddress = forms.CharField(label="宿舍地址",required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    studentClasses = forms.CharField(label='学生班级', max_length=48,widget=forms.TextInput(attrs={'class':'form-control'}))
    telephone = forms.CharField(label='Telephone', max_length=13, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    def clean_studentClasses(self):
        studentClasses = self.cleaned_data.get('studentClasses')
        result = Classes.objects.filter(name=studentClasses)
        if not result:
            raise forms.ValidationError("这个班级不存在,请输入正确的班级")
        else:
            return studentClasses
    # def clean_telephone(self):
    #     telephone = self.cleaned_data.get('telephone')
    #     result = Account.objects.filter(telephone=telephone)
    #     if  result:
    #         raise forms.ValidationError("电话号码已被注册")
    #     else:
    #         return telephone
class ProfileTeacherForm(forms.Form):  #更新老师信息
    brief = forms.CharField(label='简介', max_length=13,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
    telephone = forms.CharField(label='Telephone', max_length=13, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    # def clean_telephone(self):
    #     telephone = self.cleaned_data.get('telephone')
    #     result = Account.objects.filter(telephone=telephone)
    #     if result:
    #         raise forms.ValidationError("电话号码已被注册")
    #     else:
    #         return telephone
class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='old Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch Please enter again")

        return password2
class AddCourseForm(forms.Form):  #添加课程
    coursename = forms.CharField(label='课程名称',max_length=24,widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(
        initial='a',
        widget=widgets.Select(choices=(('a', '必修'), ('b', '选修'),),attrs={'class': 'btn btn-default'})
    )
    credit  = forms.CharField(label='学分',max_length=24,widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.CharField(label='编号', max_length=13,widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_coursename(self):
        coursename = self.cleaned_data.get('coursename')
        course = Course.objects.filter(name=coursename)
        if len(course)>0:
            raise forms.ValidationError("课程名字重复")
        return coursename
    def clean_code(self):
        code = self.cleaned_data.get('code')
        ans = Course.objects.filter(code=code)
        if len(ans)>0:
           raise forms.ValidationError("课程编码重复")
        return code

class EditCourseForm(forms.Form):  #更新课程信息
    coursename = forms.CharField(label='课程名称',max_length=24,widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(
        initial='a',
        widget=widgets.Select(choices=(('a', '必修'), ('b', '选修'),),attrs={'class': 'btn btn-default'})
    )
    credit  = forms.CharField(label='学分',max_length=24,widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.CharField(label='编号', max_length=13,widget=forms.TextInput(attrs={'class': 'form-control'}))

    # def clean_coursename(self):
    #     coursename = self.cleaned_data.get('coursename')
    #     course = Course.objects.filter(name=coursename)
    #     if len(course)>0:
    #         raise forms.ValidationError("课程名字重复")
    #     else:
    #         return coursename
    # def clean_code(self):
    #     code = self.cleaned_data.get('code')
    #     ans = Course.objects.filter(code=code)
    #     if len(ans)>0:
    #        raise forms.ValidationError("课程编码重复")
    #     else:
    #         return code

class EditTeacherDeailForm(forms.Form):  #管理员编辑教师信息
    username = forms.CharField(label='姓名', max_length=24, widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.CharField(label='工号', max_length=24,widget=forms.TextInput(attrs={'class': 'form-control'}))
    classes = forms.CharField(label="  填写新增学生班级的id", max_length=48, required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course = forms.CharField(label="填写增加教学课程的id", required=False,max_length=48, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label="电话", max_length=13,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))