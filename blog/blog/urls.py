from django.conf.urls import patterns, include, url,guest
from blogs.views import mainpage,newpost,createuser,login,logout,logincheck

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',(r'^$', mainpage),
	(r'^visit$', guestpage),
	(r'^post/new', newpost),
    (r'^account/create$', createuser),
    (r'^account/login$',  login),
    (r'^account/logout$', logout),
	(r'^account/login/check$',logincheck),
 
)
