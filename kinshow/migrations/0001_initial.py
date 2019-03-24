# Generated by Django 2.1 on 2019-03-23 16:27

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, db_column='图片', upload_to='')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('addDate', models.DateTimeField(blank=True)),
                ('updateDate', models.DateTimeField(blank=True)),
                ('state', models.IntegerField(blank=True)),
                ('commendState', models.IntegerField(blank=True)),
                ('browses', models.IntegerField(blank=True)),
                ('likes', models.IntegerField(blank=True)),
                ('comments', models.IntegerField(blank=True)),
                ('score', models.IntegerField(blank=True)),
                ('newsFile', models.FileField(blank=True, upload_to='')),
                ('isDelete', models.NullBooleanField()),
            ],
            options={
                'db_table': 'news',
                'ordering': ['updateDate'],
            },
            managers=[
                ('newsObj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='分类')),
                ('description', models.CharField(max_length=255, verbose_name='描述')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('addDate', models.DateTimeField(blank=True)),
                ('state', models.IntegerField(blank=True)),
                ('isDelete', models.NullBooleanField()),
            ],
            options={
                'db_table': 'newscategory',
                'ordering': ['id'],
            },
            managers=[
                ('categoryObj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinshow.NewsCategory'),
        ),
    ]