# 使用drf的视图集就不需要编写路由，通过DefaultRouter的register方法注册就可以了
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from App_user import views

router = DefaultRouter()
router.register('user', views.UsersView)


# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = []
urlpatterns += router.urls
