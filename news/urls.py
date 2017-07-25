from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^&', views.news_list, name='news_list'),
    url(r'^detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]