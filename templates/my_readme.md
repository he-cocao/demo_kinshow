记录:2019-3-18开始
**第一部分:基本流程**django-admin startproject projectname
1.创建工程,到settings.py配置数据库,配置完注意在__init__.py中安装pymysql.install_as_MySQLdb() 默认情况已经有了.
2.创建app,例如: 在终端输入 python manage.py startapp kinshow
3.激活APP,配置settings.py中 INSTALLED_APPS 添加 kinshow
4.在models.py去定义模型(到时候对应数据库的表,具体去models.py中有记录).
5.启动服务器,python manage.py runserver ip:port(这是python写的轻量级的web服务器,仅测试开发,ip可以不写,默认的端口是8000)
6.admin站点管理:(自觉地可以作为数据库可视化工具,也可以做后台管理,这个内容不是必须配置的)
    a.内容发布:负责添加,修改,删除内容就是指数据库的数据(可视化数据)
    b.公告访问:
    c.配置admin应用:在settings.py 中INSTALLED_APPS 默认配置了'django.contrib.admin'
    d.创建管理员用户:he_cocao bb123456
        1.createsuperuser
        2.输入用户名:不输入就是电脑用户名
        3.接着按提示输入邮箱,密码,确认密码
        4.如要进入管理页面输入:http://127.0.0.1:8000/admin
        5.汉化:setting.py 修改LANGUAGE_CODE = 'zh-Hans'  TIME_ZONE = 'Asia/Shanghai' 不行重启服务
    e.管理数据表:
        1.修改admin.py 引入模型,注册表(具体到admin.py中,实际上是装饰器注册用的多)
        2.自定义管理页面 详见admin自定义页面的DiyAdmin类
            A.列表页属性,常用4个.
            B.添加修改页属性,常用2个.
        3.关联对象,详见admin.py 第4个:添加新闻分类同时添加新闻.
        4.布尔值的处理问题见5
        5.执行动作的位置问题 actions_on_top = False   actions_on_bottom = True
7.视图:就是在views.py里面定义函数,然后定义视图后在urls.py(新建)中配置url.(这个遵循新版,不在app建立urls.py)
8.模板:就是html页面,可以根据视图中传递过来的数据进行填充 
    a.在templates中创建对应app名称的文件夹
    b.配置模板路径,在setttings中TEMPLATES下的dirs
    c.在目录下创建html文件
    d.模板语法:2种--{{里面就是python代码:输出值,变量,对象属性}}   {%里面是执行代码:比如for循环,if语句%}
    e.取数据的步骤(这个顺序按java习惯可以2.3.1) 1.写html--2.写views--3.配置url (我把这后面2个理解controller,当然业务层也在views里面写的)


**第二部分:模型**
1.Django对各种数据库都有支持,使用统一的API,对我们来说只操作模型,多种数据库交给数据库配置.
2.配置数据库,本项目以mysql为例:
    a.在__init__.py配置pymysql.install_as_MySQLdb()
    b.修改settings.py 数据库配置文件
3.开发流程还是一样的
    a.配置数据库
    b.定义模型类
    c.生成迁移文件
    d.执行迁移文件
    e.使用模型类增删改查(crud),重点在于查
4.ORM 对象-关系-映射
    a.根据对象的类型生成表结构
    b.将对象,列表的操作转换为sql语句
    c.将sql查询到的结果转换为对象,列表等
    优点:极大减轻了开发人员的工作量,不需要面对因数据库变更而修改代码.
5.定义模型(重点,详细)
    python      数据库
    模型          表
    属性          字段
    a.如果没有手动设置主键列,django会自动生成默认的主键列
    b.命名遵循标识规则,不能写连续的下划线如:he__cocao,最好不要弄下划线
    c.使用方式 导入from django.db import models 通过models.Field创建字段类型的对象,赋值给属性
    d.删除,一般都做逻辑删除,不做物理删除,实现方法就是定义一个字段-isDelete,类型为BooleanField,默认值为Flase
    e.字段类型较多,例如:CharField() 就是字符串,其他类型这里不详细写,可查资料
    f.元选项,就是class meta类,定义表描述,排序等问题
6.模型成员.Manager类型的一个对象叫objects,
    a.可以自定义管理器(基本上不用)
    b.也可以自定义Manager,可以加额外的方法,修改管理器返回的原始查询集.比如重写get_queryset()
    c.所以一般情况是先自定义管理类,再去自定义管理器(创建类似objects对象)
    d.创建对象有俩种方法,一个是在模型中写类方法,一个是在管理类中创建,调用也各有不同要注意一下,目的是为了添加数据,记得save
7.模型查询:
    a.查询集,获取的是对象的集合get_queryset(),原始的查询集是所有的数据.
    b.查询集的过滤器是为了精准查询,是基于查询条件(参数,函数)
    c.从sql语句来说,查询集等价于slecte * 语句 过滤器相对于加了where xx=
    d.查询集:
        1.管理器上自定义方法,加过滤器
        2.过滤后返回的查询集,还可以加过滤器(链式调用)
        3.惰性查询,创建查询不会带来任何数据访问,直到查询到数据的时候才会访问数据
        4.直接访问数据的情况:比如与if合用,序列化,迭代
        5.得到查询集的方法叫过滤器:
                        A.all()                                                  查所有数据
                        B.filtter(键=值) 写俩个条件都要符合,接着写的都是且,或是Q      返回符合条件的
                        C.exculde(键=值)                                         返回不符合条件的
                        D.order_by()                                                 排序
                        E.values()                                              返回列表,多个对象
    之后的详见于Django的学习笔记
    
    
浏览器(地址)--->URLS(统一资源定位符)--->视图--->模型(取数据Django学习笔记)--->模板(渲染成HTML)--->浏览器
    
Djangod的url后面如果有/,那么后在这个页面点击的都是跟着前面url添加的.如果没有就跟着项目名的路径

<h1>遗留4个问题</h1>2019-3-24记录完毕
1.redis的配置及使用.
2.富文本框的选择上,以及配置.(起码现在有DjangoUeditor,ckeditor,tinymce三种可以选择)
3.定时任务,延时问题celery的使用.
4.中间件始终没有搞明白作用.
5.轮播插件section&swiper也可以了解一下.