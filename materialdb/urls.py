from django.conf.urls import url
from materialdb import views

urlpatterns = [
    url(r'^dashboard/', views.dashboardView.as_view()),
    url(r'^user/', views.adduserView.as_view()),
    url(r'^$', views.tableView.as_view()),

]
