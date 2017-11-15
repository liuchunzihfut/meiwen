from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apply_writer/$', views.applyWrite, name='apply_writer'),
]