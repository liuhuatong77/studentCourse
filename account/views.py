from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import LoginForm, RegistrationForm, PwdChangeForm, ProfileTeacherForm, ProfileStudentForm, AddCourseForm, \
    EditCourseForm, EditTeacherDeailForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Account, Student, Classes,Course,Teacher,Admin


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                if user.account.status =='a':
                    return redirect(reverse('student_profile',kwargs={'pk':user.pk}))
                elif user.account.status == 'b':
                    return redirect(reverse('teacher_profile', kwargs={'pk': user.pk}))
                else :
                    return redirect(reverse('admin_profile', kwargs={'pk': user.pk}))
            else:
                return render(request, 'login.html', {'form': form, 'message':'Wrong password Please Try agagin'})
        else:
            return render(request, 'login.html', {'form': form, 'message':'Wrong password Please Try agagin'})
    else:
        if request.user.username:
            if request.user.account.status == 'a':
                return redirect(reverse('student_profile', kwargs={'pk': request.user.pk}))
            elif request.user.account.status == 'b':
                return redirect(reverse('teacher_profile', kwargs={'pk': request.user.pk}))
            else:
                return redirect(reverse('admin_profile', kwargs={'pk': request.user.pk}))
        form = LoginForm()
        return render(request,'login.html',{'form':form})
@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/login/')
@login_required()
def student_profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    if user.account.status == 'a':
        return render(request,'student_profile.html',{"user":user})
    else:
        return redirect('/login')

@login_required()
def teacher_profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    if user.account.status=='b':
        return render(request,'teacher_profile.html',{"user":user})
    else:
        return redirect('/login')
@login_required()
def admin_profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    if user.account.status == 'c':
        return render(request,'admin_profile.html',{"user":user})
    else:
        return redirect('/login')

def register(request):    #注册用户

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password2']
            status=form.cleaned_data['status']
            code=form.cleaned_data['code']
            user=User.objects.create_user(username=username,password=password)
            user_profile =Account(user_id=user.id, status=status, code=code)
            user_profile.save()
            if status=="a":
                student_=Student(id_id=user_profile.id,studentClasses_id=1)
                student_.save()
            elif status=="b":
                teacher_=Teacher(id_id=user_profile.id)
                teacher_.save()
            else:
                admin_ =Admin(id_id=user_profile.id)
                admin_.save()
            return HttpResponseRedirect("/login/")
        else:
            return render(request, 'register.html', {'form': form, 'message':'注册失败'})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
@login_required()
def pwd_change(request,pk):   #密码更改
    user  = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = PwdChangeForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['old_password']
            username = user.username
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                return redirect('/login/')
            else:
                return render(request,"pwd_change.html",{'form':form,'user':user,'message':'Old password is wrong try again'})
        else:
            return render(request, "pwd_change.html",{'form': form, 'user': user, 'message': 'no change success'})
    else:
        form = PwdChangeForm()
        return render(request,"pwd_change.html",{"form":form})

# @login_required()
# def profile_update(request,pk):
#     user = get_object_or_404(User,pk=pk)
#     user_profile = get_object_or_404(Account,user=user)
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST)
#         if form.is_valid():
#             user.username = form.cleaned_data['username']
#             user.save()
#             user_profile.status = form.cleaned_data['status']
#             user_profile.code = form.cleaned_data['code']
#             user_profile.telephone = form.cleaned_data['telephone']
#             user_profile.save()
#             return redirect(reverse('profile',kwargs={"pk":user.pk}))
#     else:
#         default_data={'username':user.username,'status':user_profile.status,
#                       'code':user_profile.code,'telephone':user_profile.telephone}
#         form = ProfileUpdateForm(default_data)
#     return render(request, 'profile_update.html',{'form':form})
@login_required()
def student_profile_update(request,pk):
    user = get_object_or_404(User, pk=pk)
    account_profile = get_object_or_404(Account,user=user)
    student_profile = get_object_or_404(Student,pk=account_profile.pk)
    if request.method == "POST":
        form = ProfileStudentForm(request.POST)
        if form.is_valid():
            try:
                account_profile.telephone = form.cleaned_data['telephone']
                account_profile.save()
                student_profile.studentAddress = form.cleaned_data['studentAddress']
                studentClassesName = form.cleaned_data['studentClasses']
                class_ = Classes.objects.get(name=studentClassesName)

                student_profile.studentClasses=class_
                student_profile.save()
                return redirect(reverse('student_profile',kwargs={"pk":user.pk}))
            except:
                return render(request,'student_profile.html',{'user':user,'message':'更新信息失败'})
        else:
            default_data = {'telephone': account_profile.telephone, 'studentAddress': student_profile.studentAddress,
                            'studentClasses': student_profile.studentClasses.name}
            form = ProfileStudentForm(default_data)
            return render(request, 'profile_update.html', {'form': form, 'user': user})

    else:
        default_data={'telephone':account_profile.telephone,'studentAddress':student_profile.studentAddress,
                      'studentClasses':student_profile.studentClasses.name}
        form = ProfileStudentForm(default_data)
        return render(request,'profile_update.html',{'form':form,'user':user})

def teacher_profile_update(request,pk):
    user = get_object_or_404(User, pk=pk)
    account_profile = get_object_or_404(Account,user=user)
    teacher_profile = get_object_or_404(Teacher,pk=account_profile.pk)
    if request.method == "POST":
        form = ProfileTeacherForm(request.POST)
        if form.is_valid():
            account_profile.telephone = form.cleaned_data['telephone']
            account_profile.save()
            teacher_profile.brief = form.cleaned_data['brief']
            teacher_profile.save()
            return redirect(reverse('teacher_profile',kwargs={"pk":user.pk}))
    else:
        default_data={'telephone':account_profile.telephone,'brief':teacher_profile.brief}
        form = ProfileTeacherForm(default_data)
        return render(request,'profile_update.html',{'form':form,'user':user})
@login_required()
def classes_student(request,pk):   #通过学生id查询到学生所在班级和班级所以学生信息
    st1 = get_object_or_404(Student, pk=pk)
    class1 = st1.studentClasses.name
    st_all = st1.studentClasses.student_set.all()
    return render(request, 'classes_student.html', {'st_all':st_all,'class1':class1})


@login_required()
def classes_all(request,pk):    #通过班级id查询班级全部学生信息
    classes = get_object_or_404(Classes,pk=pk)
    class1 = classes.name
    st_all = classes.student_set.all()
    print(st_all)
    return render(request, 'classes_student.html',{'st_all':st_all,'class1':class1})

@login_required()
def edit_teacher_all(request):
    all_teacher=Teacher.objects.all()
    return render(request,'admin_edit_teacher_all.html',{"all_teacher":all_teacher})

@login_required()
def add_course(request):      #添加课程
    if request.method=="POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            coursename = form.cleaned_data['coursename']
            type = form.cleaned_data['type']
            code = form.cleaned_data['code']
            credit= form.cleaned_data['credit']
            course = Course(name=coursename,type=type,code=code,credit=credit)
            course.save()
            return redirect(reverse('admin_profile',kwargs={"pk":request.user.id}))
        else:
            return render(request, 'add_course.html', {'form': form, 'message': '添加课程失败'})
    else:
        form = AddCourseForm()
        return render(request,'add_course.html',{'form':form})
@login_required()
def all_course(request):  #查看全部课程
    courses=Course.objects.all()
    return render(request,'all_course.html',{'courses':courses})
@login_required()
def course_detail(request,pk):  #课程详情
    course = Course.objects.get(pk=pk)
    teachers = course.courseTeacher.all()
    return render(request,'course_detail.html',{'course':course,'teachers':teachers})

def edit_course(request,pk):  #编辑课程
    course = Course.objects.get(pk=pk)
    if request.method=='POST':
        form = EditCourseForm(request.POST)
        if form.is_valid():
            course.name = form.cleaned_data['coursename']
            course.type = form.cleaned_data['type']
            course.code = form.cleaned_data['code']
            course.credit = form.cleaned_data['credit']
            course.save()
            return redirect(reverse('all_course'))
        else:
            default = {'coursename': course.name, 'code': course.code, 'credit': course.credit, 'type': course.type}
            form = EditCourseForm(default)
            return render(request, 'edit_course.html', {'form': form,'message':'更新课程失败'})
    else:
        default={'coursename':course.name,'code':course.code,'credit':course.credit,'type':course.type}
        form = EditCourseForm(default)
        return render(request,'edit_course.html',{'form':form})

def admin_edit_detail(request,pk):
    account_ =Account.objects.get(pk=pk)
    user_ = User.objects.get(id = account_.user.id)
    teacher_ = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditTeacherDeailForm(request.POST)
        if form.is_valid():
            user_.username= form.cleaned_data['username']
            user_.save()
            account_.code = form.cleaned_data['code']
            if form.cleaned_data['telephone']:
                account_.telephone = form.cleaned_data['telephone']
            account_.save()
            if form.cleaned_data['classes']:
                class_id= form.cleaned_data['classes']
                class_ = get_object_or_404(Classes,pk=int(class_id))
                class_.classesTeacher.add(teacher_)
                class_.save()
            if form.cleaned_data['course']:
                course_id = form.cleaned_data['course']
                course_ = get_object_or_404(Course,id = int(course_id))
                course_.courseTeacher.add(teacher_)
                course_.save()
            return redirect(reverse('edit_teacher_all'))
        else:
            default = {'username':account_.user.username,'code':account_.code,'telephone':account_.telephone,
                       }
            form = EditTeacherDeailForm(default)
            return render(request,'admin_edit_teacher_detail.html',{'form':form})
    else:
        default = {'username': account_.user.username, 'code': account_.code, 'telephone': account_.telephone,
                   }
        form = EditTeacherDeailForm(default)
        return render(request, 'admin_edit_teacher_detail.html', {'form': form})

def edit_class_all(request):  #查看全部班级信息
    classes = Classes.objects.all().order_by('id')
    return render(request, 'edit_classes_all.html', {"classes":classes})


def edit_class_student (request,pk):    #传入班级id
    class1 = Classes.objects.get(pk=pk)
    st_all = class1.student_set.all()
    classname = class1.name
    return render(request, 'edit_classes_student.html', {'st_all': st_all, 'classname': classname})


