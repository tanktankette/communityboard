from django.conf.urls import url
from community_calendar import views

app_name = 'community_calendar'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<month>[\d]+)$', views.index),
    url(r'^(?P<month>[\d]+)/(?P<year>[\d]+)$', views.index),
]
