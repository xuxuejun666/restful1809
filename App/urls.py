from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt #过滤csrf

from . import views
urlpatterns = [
    url(r'^user/$',csrf_exempt(views.UserTest.as_view()),name='usertest'),
]