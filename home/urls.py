from django.conf.urls import url,include
from home.views import *

urlpatterns = [
  url(r"^$",main),
  url(r"^submenu/$", submenu),
]
