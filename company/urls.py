from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^compform$', views.com_form, name="compform")
]