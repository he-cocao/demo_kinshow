from django.contrib import admin
##############################################################################
# 1.引入模型
from kinshow.models import NewsCategory, News,Article
admin.site.register(Article)

##############################################################################
# 3.自定义页面,注意如果要使用这个自定义的,注册的时候要继承该类
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ["id", "title", "category", "description"]  # 显示字段的
    list_filter = ["category"]  # 过滤字段,把重复的拿出来
    search_fields = ["description"]  # 按里面的内容搜索的字段
    list_per_page = 5  # 分页
    # 添加,修改页属性,下面2个不能同时使用,一般情况用fieldsets
    # fields = ["category"]  # 改变显示顺序的,默认是按先后的,注意的是这里写几个就显示几个,默认都是显示的
    fieldsets = [
        ("base", {"fields": ["title", "description", "image", "category"]}),
        ("base_time", {"fields": ["updateDate", "addDate", "score", "state"]})
    ]  # 给属性分组的

##############################################################################
# 4.需求:创建新闻分类的时候就可以创建2条新闻
class NewsInfo(admin.StackedInline):  # TabularInline横向显示,StackedInline纵向显示
    model = News
    extra = 1  # 这里是news的个数

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    # 承接4,这里的意思是加俩行新闻
    inlines = [NewsInfo]


##############################################################################
# 5布尔值的处理问题,写个方法,在将方法写入list_display中(写入不是方法,是属性)
    def judge_boolean(self):
        if self.name:
            return "好"
        else:
            return "坏"

    # name.short_description = "分类" 这是修改列的名称,该名称还可以在models中修改

    # 列表页属性
    list_display = ["id", "name", "description", "addDate"]  # 显示字段的
    list_filter = ["name"]  # 过滤字段,把重复的拿出来
    search_fields = ["name"]  # 按里面的内容搜索的字段
    list_per_page = 5  # 分页
    # 添加,修改页属性,下面2个不能同时使用,一般情况用fieldsets
    fields = ["description", "name", "addDate","state"]  # 改变显示顺序的,默认是按先后的,注意的是这里写几个就显示几个,默认都是显示的
    # fieldsets = [
    #     ("base", {"fields": ["description", "image", "category"]}),
    #     ("base_time", {"fields": ["updateDate", "addDate", "score", "state"]})
    # ]  # 给属性分组的

    # 执行动作条的位置top在上,bottom在下
    actions_on_top = False
    actions_on_bottom = True


##############################################################################
# 2.Register your models here.注册表,默认情况如下,现在放出自定义的,真实情况是用装饰器注册如:在自定义类上加@admin.register(NewsCategory)
# admin.site.register(News)
# admin.site.register(NewsCategory)
# admin.site.register(News, NewsAdmin)
# admin.site.register(NewsCategory, NewsCategoryAdmin)
