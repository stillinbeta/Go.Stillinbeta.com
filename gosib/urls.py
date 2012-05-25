from django.conf.urls.defaults import patterns, include, url

from go.views import handle_home, follow_redirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', handle_home),
    url(r'^(?P<word>[a-z]*)$', follow_redirect),
    ('^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/sib/Devel/gosib/gosib/static'})
)
