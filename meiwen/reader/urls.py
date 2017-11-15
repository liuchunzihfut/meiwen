from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fill_information/$', views.fill_in_personal_information, name='fill_information'),
]