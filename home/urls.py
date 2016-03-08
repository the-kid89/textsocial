from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [url(r'^$', csrf_exempt(views.Index.as_view()), name='index'), ]
