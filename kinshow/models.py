from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
"""
1.不需要写主键,主键自动增加,这里有疑问,是否是在数据库中定义主键并默认自动增加(实践证明不能写主键,或者加primary_key=True)
2.可在这里头生成数据库表:(python manage.py 可以在tools下面找到 Run  manage.py Task...)
    a.生成迁移文件   python manage.py makemigrations  在该文件下会生成0001_initial.py文件(迁移文件)
    b.执行迁移      python manage.py migrate 相当于执行sql语句创建表,但是这数据库名要注意(不能重复名)
    c.默认表名会加上项目名例如:kinshow_news
3.测试数据操作:
    a.进入shell  如果要退出输入:quit()
    b.引入包 
        from django.utils import timezone
        from datetime import *
        from kinshow.models import News,NewsCategory
        News.objects.all() 可以看到数据库中所有的数据
    c.添加数据,本质是添加模型数据的对象实例
        news_part=News()        创建对象
        news_part.browses=2     赋值
        news_part.save()        保存
    d.查询数据 News.objests.get(pk=2)这里pk就是主键
    e.修改数据 就是另外赋值(对象名.属性) 记得保存
    f.删除数据 news_part.delete() 物理删除(真删)整条数据
    g.关联对象 
        注意外键的设置这里的例子可以这样些 news_part.category = newscategory1 (这里newscategory1是对象)
        实例:查询一个分类的所有新闻 newscategory.news_set.all()  (news_set是自带的属性,可以看出来这是个集合)
     
"""


# 自定义Manger用于重写方法的
class NewsManager(models.Manager):
    def get_queryset(self):
        # filter(isDelete=False)过滤的算是重写的部分
        return super(NewsManager, self).get_queryset().filter(state=1)

    ########################################################################################
    # 创建对象第二种办法:在自定义管理类中加加方法创建对象,这里继承的是Manager
    def createNews(self, title, description, author):
        news = self.model()
        news.description = description
        news.title = title
        news.author = author
        # 到时候调用是这样的
        # News.newsObj.createNews(title,description,author)
        return news


class News(models.Model):
    # 自定义管理器2 创建了新的管理器类
    newsObj = NewsManager()
    # id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # 这里一对多的关系,一个新闻分类有多个新闻,顾这里新闻分类写外键
    # category = models.CharField(max_length=255)
    category = models.ForeignKey("NewsCategory", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, db_column="图片")
    # content = models.TextField(blank=True)
    content = UEditorField(width=600, height=300,
                           toolbars="full",
                           imagePath="images/",
                           filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    addDate = models.DateTimeField(blank=True)  # 里面的参数表示第一次添加的时间,自动设置auto_created=True
    updateDate = models.DateTimeField(blank=True)  # 里面的参数表示最后一次修改,自动设置auto_now=True
    state = models.IntegerField(blank=True)
    commendState = models.IntegerField(blank=True)
    browses = models.IntegerField(blank=True)
    likes = models.IntegerField(blank=True)
    comments = models.IntegerField(blank=True)
    score = models.IntegerField(blank=True)
    newsFile = models.FileField(blank=True)
    isDelete = models.NullBooleanField()

    # 重新str方法
    def __str__(self):
        return self.title

    # 元选项
    class Meta:
        db_table = "news"
        ordering = ["updateDate"]

    ########################################################################################
    # 创建对象第一种方法:定义一个类方法创建对象如果不是使用注解,父类就写上News类,这里继承的moles
    @classmethod
    def createNews(cls, titile, description):
        news = cls(titile=titile, description=description)
        return news


class NewsCategory(models.Model):
    # 自定义管理器1 这个categoryObj就是之前的objests
    categoryObj = models.Manager()
    # id = models.CharField(max_length=255)
    # verbose_name,包括第一个字段设置"分类"这种情况,都是类似在数据库重命名列的名称
    name = models.CharField("分类", max_length=255)
    description = models.CharField(verbose_name="描述", max_length=255)
    image = models.ImageField(blank=True)
    addDate = models.DateTimeField(blank=True)
    state = models.IntegerField(blank=True)
    isDelete = models.NullBooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "newscategory"
        ordering = ["id"]  # 默认是升序,降序加-





# 下面的类中content可以做富文本框的范例
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = UEditorField(width=600, height=300,
                           toolbars="full",
                           imagePath="images/",
                           filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
