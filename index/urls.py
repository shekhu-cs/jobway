from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'^homepage$', views.homepage, name="homepage"),
    url(r'^jobresult$', views.results, name="jobresult"),
    url(r'^search/$', views.search,),



]

