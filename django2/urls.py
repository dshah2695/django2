from django.conf.urls import url
from django.contrib import admin
from firstwebapp import views

urlpatterns = [
    url(r'^invalid/$', views.invalid_login),
    url(r'^home/$', views.home_page),
    url(r'^loginform/$', views.login_form ),
    url(r'^time/$', views.Display_date_time ),
    url(r'^$', views.index ),
    url(r'^admin/', admin.site.urls),
]
