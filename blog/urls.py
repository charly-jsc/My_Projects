from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('snippet', views.snippet_detail),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
