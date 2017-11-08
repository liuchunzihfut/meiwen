from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.userLogin, name='login'),
    url(r'^sign_up/', views.signUp, name='signUp'),
    url(r'^change_password/', views.changePassword, name='changePassword'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^test/', views.test, name='test'),
]