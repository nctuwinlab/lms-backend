from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.MemberProfile.as_view(), name='profile'),
]
