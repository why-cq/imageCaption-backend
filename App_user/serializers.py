from rest_framework import serializers

from .models import Users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定序列化器对应的模型
        model = Users
        # 指定需要序列化的字段，‘__all__’表示所有字段
        fields = "__all__"
