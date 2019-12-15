from django.conf.urls import url
from . import views
from django.contrib.auth.views import (login, logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete)

urlpatterns = [
    # or you can make it views.home, name = "home" and make corresponding change in views.py
     #url(r'^$', views.index, name='index'),   
     url(r'^$', views.homepage, name='homepage'), 

     url(r'^clubinfo/$', views.clubinfo, name='clubinfo'), 
     url(r'^courseinfo/$', views.courseinfo, name='courseinfo'), 
     url(r'^freeride/$', views.freeride, name='freeride'), 
     url(r'^privatetutor/$', views.privatetutor, name='privatetutor'), 
     url(r'^rentinfo/$', views.rentinfo, name='rentinfo'), 

    #render to template_name
    url(r'^login/$', login ,{'template_name':'accounts/login.html'}, name='login'), 
    url(r'^logout/$', logout ,{'template_name':'accounts/logout.html'}, name='logout'), 
    url(r'^register/$', views.register, name='register'),

    url(r'^profile/$', views.viwe_profile, name='viwe_profile'),
    url(r'^profile/edit/$', views.edit_profile,  name="edit_profile"),   
    
    url(r'^change-password/$', views.change_password, name = "change_password"),
    url(r'^reset-password/$', password_reset,
    {'template_name':'accounts/reset_password.html','post_reset_redirect': 'InfoTrack:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'} , 
    name = "reset_password"),
    
    url(r'^reset-password/done$', password_reset_done,{'template_name': 'accounts/reset_password_done.html'}, name = "password_reset_done"),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,{'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'InfoTrack:password_reset_complete'} ,name = "password_reset_confirm"),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name = "password_reset_complete"),
    
    url(r'^add_post.html/$', views.add_post, name='add_post'),
    url(r'^post_list.html/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^add_comment.html/(?P<pk>\d+)$', views.add_comment, name='add_comment'),
    url(r'^post_search.html/$', views.post_search, name='post_search'),

    url(r'^view_friends/(?P<username>[\w-]+)$', views.view_friends, name = "view_friends"),
    url(r'^add_friend/(?P<to_username>[\w-]+)$',views.friendship_add_friend,name="add_friend"),
    url(r'^friend/requests/$',views.friendship_request_list,name="friendship_request_list"),
]   

#python3 -m smtpd -n -c DebuggingServer localhost:1025
