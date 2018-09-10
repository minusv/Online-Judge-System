from django.conf.urls import url,include
from . import views


urlpatterns=[
    url(r'^contest/$', views.contestant_home, name='home'),
    url(r'^contest/submit/', views.submit_code, name='submit'),
    url(r'^contest/status/', views.view_status, name='status'),
] 
