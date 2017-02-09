from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'bot/(?P<endpoint>.+)$', views.bot, name='bot'),
]
