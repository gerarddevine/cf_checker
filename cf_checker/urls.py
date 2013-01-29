from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                           
    # admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # home and about pages
    (r'^$','cf_checker.apps.cfchecker.views.home', {}, 'home'),
    (r'^about/$','cf_checker.apps.cfchecker.views.about', {}, 'about'),
    (r'^news/$','cf_checker.apps.cfchecker.views.news', {}, 'news'),
)


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^static/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True }),
    (r'^media/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),
    )
