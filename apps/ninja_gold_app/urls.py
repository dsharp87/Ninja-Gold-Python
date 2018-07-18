from django.conf.urls import url
from . import views 

print "im in apps urls"

#ninja_gold_app file
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.process),
    url(r'^reset$', views.reset)
]