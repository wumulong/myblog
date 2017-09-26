from django.conf.urls import url
from .views import index, detail


app_name = 'blog'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^detail/', detail, name='detail'),
]