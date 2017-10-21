from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.ArticleList.as_view()),
    url(r'^subjects/$', views.SubjectList.as_view()),
    #url(r'^list/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),

]
