"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app01 import views
from django.views.static import serve
from django.conf import settings
from app01.views import upload_list

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root: settings.MEDIA_ROOT'}, name='media'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/add/', views.homepageadd,name='homepageadd'),
    path('homepage/delete/', views.homepagedelete,name='homepagedelete'),
    path('details/delete/', views.detailsdelete,name='detailsdelete'),
    path('details/<int:nid>', views.details, name='details'),
    path('boy/', views.boy, name='boy'),
    path('boy/details/<int:nid>', views.boydetails, name='boydetails'),
    path('girl/', views.girl, name='girl'),
    path('girl/details/<int:nid>', views.girldetails, name='girldetails'),
    path('random/', views.randoms, name='random'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('comment/<int:nid>', views.comment, name='comment'),
    path('boy/comment/<int:nid>', views.boycomment, name='boycomment'),
    path('girl/comment/<int:nid>', views.girlcomment, name='girlcomment'),
    path('random/comment/<int:nid>', views.randomcomment, name='randomcomment'),
    path('profile/', views.profile, name='profile'),
    path('record/', views.record, name='record'),
    path('comment/delete/', views.commentdelete, name='commentdelete'),
    path('girl/delete/', views.girldelete, name='girldelete'),
    path('boy/delete/', views.boydelete, name='boydelete'),
    path('random/delete/', views.randomdelete, name='randomdelete'),
    path('user/history/', views.user_history, name='user_history'),
    path('register/', views.register, name='register'),
    path('upload/list/', views.upload_list, name='upload_list')
]
