from django.conf.urls import url
from .views import IndexView, SimpleView

urlpatterns = [
    url('simple/(?P<name>.*)', SimpleView.as_view()),
    url('(?P<name>.*)', IndexView.as_view()),
]
