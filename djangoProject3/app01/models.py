from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
# Create your models here.
class info_list(models.Model):
    name = models.CharField(verbose_name='昵称', max_length=16)
    describe = models.CharField(verbose_name='描述', max_length=64)
    money = models.IntegerField(verbose_name='价格')
    inventory = models.IntegerField(verbose_name='库存')
    # gender_choices = (
    #     (1, '男'),
    #     (2, '女'),
    # )
    # gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
class admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

class comment(models.Model):
    text = models.TextField(verbose_name='用户名', max_length=32)
    comment_time = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=64)
    class Meta:
        ordering = ['-comment_time']

from django.db import models
from django.contrib.auth.models import User

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)