from django.conf.urls import include, url
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$',views.login),
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),

    url(r'^list/$',views.listing),
    url(r'^post/$',views.posting),
    url(r'^post2db/$',views.post2db),
    url(r'^contact/$',views.contact),
]
