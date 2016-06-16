from django.conf.urls import url
from . import views

#adding urls here

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
