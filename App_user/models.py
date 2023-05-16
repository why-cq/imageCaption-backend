from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    phone = models.CharField(max_length=100, verbose_name="手机号")
    sex = models.CharField(max_length=2, default="男", verbose_name="性别")
    id_number = models.CharField(max_length=18, null=True, verbose_name="身份证号")
    status = models.IntegerField( default=1, verbose_name="账号状态")  # 0表示禁用,1表示正常
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'why_users'
        ordering = ['id']



