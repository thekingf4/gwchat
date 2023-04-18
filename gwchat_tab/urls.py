# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.conf import settings
from .views import GWCHATView


urlpatterns += (
    url(
        r'^courses/{}/gwchat/'.format(
            settings.COURSE_ID_PATTERN,
        ),
        GWCHATView.as_view(),
        name='gwchat_view',
   ),
 )