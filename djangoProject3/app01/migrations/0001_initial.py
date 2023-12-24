# Generated by Django 2.2.4 on 2023-11-21 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='昵称')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('hobby', models.CharField(max_length=64, verbose_name='个人简介')),
                ('phone', models.IntegerField(verbose_name='电话号码')),
                ('home', models.CharField(max_length=16, verbose_name='住址')),
                ('gender', models.SmallIntegerField(choices=[('1', '男'), ('2', '女')], verbose_name='性别')),
            ],
        ),
    ]
