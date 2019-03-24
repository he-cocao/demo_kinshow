from django.db import models


# Create your models here.
class News(models.Model):
    # id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # 这里一对多的关系,一个新闻分类有多个新闻,顾这里新闻分类写外键
    # category = models.CharField(max_length=255)
    category = models.ForeignKey("NewsCategory", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, db_column="图片")
    content = models.TextField(blank=True)
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

    @classmethod
    def createNewscategory(cls, name, description):
        newscategory = cls(name=name, description=description)
        return newscategory
