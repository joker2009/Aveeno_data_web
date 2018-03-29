__author__ = 'joker_jiang'

"""定义data_web的URL模式"""

from django.conf.urls import url

from . import views
from django.contrib.auth.views import login

urlpatterns = [

    url(r'^login/$', login, {'template_name': 'login.html'},
        name='login'),
    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),

]