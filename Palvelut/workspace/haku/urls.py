from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kartta$', views.kartta, name='haku'),
    url(r'^historia$', views.historia, name='historia'),
    url(r'^search$', views.search_new, name='search'),
]