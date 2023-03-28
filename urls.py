from django.conf.urls import  url
from django.contrib.auth.decorators import login_required

from .views import gwchat_view
urlpatterns = [
    url(r"^/$", gwchat_view , name="gwchat_view")
]


