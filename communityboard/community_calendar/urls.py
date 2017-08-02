from django.conf.urls import url
from community_calendar import views

app_name = 'community_calendar'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
