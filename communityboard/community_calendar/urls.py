from django.conf.urls import url
from community_calendar import views

app_name = 'community_calendar'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<month_year>[\d]+-[\d]+)$', views.index, name='index'),
    url(r'^(?P<event_id>[\d\w]+)$', views.event_detail, name='event_detail')
]
