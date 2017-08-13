from django.conf.urls import url
from messageboard import views

app_name = 'messageboard'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)$', views.board, name='board'),
]
