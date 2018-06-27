from django.conf.urls import url
from materialdb import views

urlpatterns = [
    url(r'^$', views.tableView.as_view()),
    url(r'^adduser', views.adduserView.as_view()),
    url(r'^edit', views.edituserView.as_view()),

]
