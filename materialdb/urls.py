from django.conf.urls import url
from materialdb import views

urlpatterns = [
    url(r'^$', views.dashboardView.as_view()),
    url(r'^user/', views.adduserView.as_view()),
    url(r'^table/', views.tableView.as_view()),

]
