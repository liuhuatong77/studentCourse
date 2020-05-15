"""studentCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),   #登陆
    path('register/', views.register, name='register'),  # 注册
    path('logout/', views.logout, name='logout'),   #注销
    path('pwd_change/<int:pk>/', views.pwd_change, name='pwd_change'),  # 更改密码
    path('user/<int:pk>/student/profile/', views.student_profile,name='student_profile'),  #学生信息
    path('user/<int:pk>/teacher/profile/', views.teacher_profile, name='teacher_profile'), #老师信息
    path('user/<int:pk>/admin/profile/', views.admin_profile, name='admin_profile'),        #管理员信息
    path('user/<int:pk>/student/class/students/', views.classes_student, name='classes_student'),   #查询学生所在班级的学生信息
    path('user/<int:pk>/teacher/class/students/',views.classes_all,name='classess_all'),      #查询老师所教班级的学生信息
    path('user/admin/edit/teacher_all/',views.edit_teacher_all, name="edit_teacher_all"),  #查询全部教师
    path('user/edit/edit_classes_all/', views.edit_class_all, name="edit_class_all"),  #查看全部班级信息
    path('user/edit/class_classes_all/<int:pk>/class/student/', views.edit_class_student, name="edit_class_student"), #管理员某班级全部学生信息
    path('user/admin/edit/<int:pk>/detail/', views.admin_edit_detail, name="edit_teacher_detail"),
    path('user/<int:pk>/profile/student/update',views.student_profile_update,name='student_profile_update'), #学生信息更新
    path('user/<int:pk>/profile/teacher/update', views.teacher_profile_update, name='teacher_profile_update'),  #老师信息更新
    path('user/add/course/', views.add_course, name="add_course"),  # 添加课程
    path('user/all/course/', views.all_course, name="all_course"),  #全部课程
    path('user/all/course/<int:pk>/', views.course_detail, name="course_detail"),  #课程详情
    path('user/all/course/<int:pk>/edit', views.edit_course, name="edit_course"),  # 课程详情
    path('captcha', include('captcha.urls'))                                                #验证码配置
    # re_path(r'^register/$', views.register, name='register'),
    # re_path(r'^login/$', views.login, name='login'),
    # re_path(r'^user/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    # re_path(r'^user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    # re_path(r'^user/(?P<pk>\d+)/pwd_change/$', views.pwd_change, name='pwd_change'),
    # re_path(r"^logout/$", views.logout, name='logout'),
]
