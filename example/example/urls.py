from django.conf.urls import url
from .views import IndexView

urlpatterns = [
    url('(?P<name>.*)', IndexView.as_view()),
]
