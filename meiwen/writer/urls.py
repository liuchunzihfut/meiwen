from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apply_writer/$', views.applyWrite, name='apply_writer'),
    url(r'^create_group/$', views.creatGroup, name='creat_group'),
    url(r'^apply_group/$', views.applyGroup, name='apply_group'),
    url(r'^reply_apply/$', views.replyApply, name='reply_apply'),
    url(r'^my_apply/$', views.myApplyShow, name='my_apply_show'),
    url(r'^other_apply/$', views.otherApplyShow, name='other_apply_show'),
]