# 学生信息管理系统(初学者学习django)
项目除了学习参考django,没什么实际用处
##环境 
django3,python3.8,mysql,linux(我是在linux下写的,但对windows应该无影响,这项目就是初学django练习没环境要求)
本人是练习一些原因,项目包没有用虚拟环境,所以导出的requestment.txt可能有一些不是项目必要的包
## 实现功能
简单实现了登陆注册,身份有三个学生,老师管,理员,项目还完善,能给初学着一些参考   
查询添加更新学生老师信息,课程信息,班级信息.这些连表的增删改查,删没写
## 数据库表格
有学生表,老师表,管理员表,课程表,班级表,用户表(看起来挺多的,但是有很多复杂的没有的关系没有实现,但是当作初学django足够)   
一开始设计表关系时用些不合理,添加更改字段时终于明白了关系型数据库,变更表结构的难
## 使用
1. 项目导入本地  
2. 进去项目文件夹,先安装依赖pip install -r requestment.txt   
3. 更该setting数据库配置(本人数据库没价值,密码没改)  
4. 执行下面两个命令  
    python manage.py makemigrations
    python manage.py migrate
5. 执行python manage.py runserver 0.0.0.0:8000运行项目  
6. 访问http://127.0.0.1:8000/login/即可
## 下面是一些项目运行图片
![](file:///home/test/Desktop/1.png)
![](file:///home/test/Desktop/2.png)
![](file:///home/test/Desktop/3.png)
![](file:///home/test/Desktop/4.png)
![](file:///home/test/Desktop/9.png)
![](file:///home/test/Desktop/5png)
![](file:///home/test/Desktop/6.png)
![](file:///home/test/Desktop/7.png)
![](file:///home/test/Desktop/8.png)
# 项目详解
1. 使用Django Auth自带的User模型进行扩展了一个用户表account,account又分别一对一了学生表student,  
教师表teacher,管理员表.所以我在注册用户时,要分别在自带User表保存,和用户表account保存和account  
表一对一的表保存. 
2. 
```
    #判断表单是否合法
        form = LoginForm(request.POST)
        if form.is_valid(): 
    #登录时验证用户名和密码是否与数据库中的相同,如果条件成立,会返回一个user对象
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
    # create_user()函数创建一个经过加密的一个密码
        user = NewUser.objects.create_user(username=username,email=email,password=password1)
    # @login_required放到函数上面,要求先登录,才能访问视图函数
        @login_required
        def article(request,article_id):

        在settings中设置LOGIN_URL = '/accounts/login/' #如果用户还没有登录，默认会跳转这路径
    # 退出登陆
        def logout(request)
            auth.logout(request)
            return Redirect("/login/")
    #request.path  拿到的路径是/index/,不包括参数
    # get_full_path() 获取路由的完整地址,包括参数
        res = request.get_full_path()
    # get_object_or_404() 捕获异常函数,如果对象不存在,就显示django内置404页面展示给用户
        article_obj = get_object_or_404(Article,id=article_id)
```
3 .     
```
## reverse反转并且传递参数和反转url
    在urls中
    path('user/<int:id>/profile/', views.profile,name='profile'),
    情况一:
        在views中使用reverse反转
         return redirect(reverse('profile',kwargs={'id':user.id}))
    情况二:
        #使用include分发路由(本项目太小没有在用这个include分发路由)
            url(r'^polls/', include('polls.urls', namespace='polls')),
            return redirect(reverse('polls:profile',kwargs={'id':user.id}))   #这个profile是polls.url中的一个path参数的name
    情况三:
        在html中
        使用命名url
        <a href="{%  url  'profile'  id %}Article</a>
```
4
```
在forms.py中
### 通过def clean_name(self):  重写username字段自定义表单验证
    def clean_username(self):
        username = self.cleaned_data.get('username')   # 获取到前端表单username的值
        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError('This username does not exist Please register first')
        else:
            return username

```
5
```
## captcha 登陆时图形验证码的使用
    1.安装pip install django-simple-captcha
    2.在INSTALLED_APPS 里添加'captcha'
    3.python manage.py migrate 在数据库建立表
    4.在urls.py文件中增加captcha对应的网址： path('captcha', include('captcha.urls'))
    5.在forms表单中添加captcha = CaptchaField(label='验证码')
```
6
### 自定义过滤器
    本项目中,三个身份学生,老师,管理员,对应存储分别为a,b,c.
    在页面中查到的对应的是a,b,c字母.我们用过滤器把这个字母转化为对应的身份
    
    自定义过滤器使用方法,这里以一个身份过滤例子来说:
    1.在某个app下创建一个templatetags(与models.py是同级)
    2.在templatetags文件夹下,新建空文件 __init__.py(这是python的规矩,__init__.py表示其所在的文件夹是一个可以载入的模块,__init__文件内容可为空)
    3.新建一个status_tags.py函数
        from django.template import Library
        register = Library()
        @register.filter
        def status_tags(status):
            if status == 'a' :
                return '学生'
            elif status == 'b':
                return '老师'
            else :
                return '管理员'
    4.在html中添加{% load status_tags %}
    5.在settings中添加
        TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            'libraries':{                                  #你的过滤器列表
                    "status_tags": "app.templatetags.status_tags",   #你过滤器的位置
                },
            },
        },
    ]