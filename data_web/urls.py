__author__ = 'joker_jiang'

"""定义data_web的URL模式"""

from django.conf.urls import url

from . import views
from django.contrib.auth.views import login

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),  # 返回request类型
    # 登录界面
    # url(r'^login/$', login, {'template_name': 'login.html'},
    #     name='login'),
    url(r'^register/$', views.change_pass, name='change_pass'),
    # 注销

    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'output', views.output),
    url(r'down/', views.down),

    url(r'^search/$', views.search, name='search')
]