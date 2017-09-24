from django.conf.urls import include, url
from django.conf.urls.static import static
from rest_framework.authtoken import views
from . import views

urlpatterns = [


    url(
        regex=r'^$',
        view=views.userlist,
        name="userlist"
    ),
    url(
        regex=r'^(?P<user_id>\d+)/$',
        view=views.userdetails,
        name="userdetails"
    ),
    url(
        regex=r'^/$',
        view=views.usercreate,
        name="userdetails"
    ),
    url(
        regex=r'^(?P<user_id>\d+)/$',
        view=views.userdelete,
        name="userdetails"
        )
    ]
