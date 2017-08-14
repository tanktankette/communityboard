from django.conf.urls import url
from tasklist import views

app_name = 'tasklist'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check$', views.check, name='check'),
]
