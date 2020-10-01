from . import views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('thinkcenter/', views.thinkCenter, name='thinkcentre'),
    path('thinkstation/', views.thinkstation, name='thinkstation'),
    path('thinkpad/', views.thinkpad, name='thinkpad'),
    path('esports/', views.esports, name='esports'),
    path('campuscomputing/', views.campuscomputing, name='campuscomputing'),
    path('securityandservices/', views.securityandservices, name='securityandservices'),
    path('datacentered/', views.datacentered, name='datacentered'),



    path('post/thinkcentre/', views.postDataThinkcentre, name='postDataThinkcentre'),
    path('post/thinkstation/', views.postDataThinkstation, name='postDataThinkstation'),
    path('post/thinkpad/', views.postDataThinkpad, name='postDataThinkpad'),
    path('post/esports/', views.postDataEsports, name='postDataEsports'),
    path('post/campuscomputing/', views.postDataCampuscomputing, name='postDataCampuscomputing'),
    path('post/securityandservices/', views.postDataSecurityandservices, name='postDataSecurityandservices'),
    path('post/datacentered/', views.postDataDatacentered, name='postDataDatacentered'),
    ]