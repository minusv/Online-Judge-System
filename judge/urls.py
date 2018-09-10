from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'judge/$', views.judge_home, name='judge_home'),
    url(r'judgestatus/$', views.judge_status, name='judge_status'),
    url(r'question/add/$', views.add_question, name='add_question'),
    url(r'question/view/$', views.view_question, name='view_question'),
    url(r'question/edit/(?P<pk>\d+)/$', views.edit_question, name='edit_question'),
    url(r'question/delete/(?P<pk>\d+)/$', views.delete_question, name='delete_question'),
] 
