from django.conf.urls import url
from materialdb import views

urlpatterns = [
    url(r'^$', views.tableView.as_view()),
    url(r'^adduser', views.addpersonView.as_view()),
    url(r'^edit', views.editpersonView.as_view()),

]
