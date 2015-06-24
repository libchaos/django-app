from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import hello_world, home, post_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'post/(?P<id>\d+)', post_detail, name="post_detail"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello_world)
)
