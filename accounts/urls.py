from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import logout


urlpatterns=[
    url(r'^$',views.redirect_to_login, name='redirect'),
    url(r'^register/', views.register_user, name='register'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^logout/', logout, {'next_page': '/login'}),
]