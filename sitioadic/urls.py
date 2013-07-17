from django.conf.urls import patterns, include, url
from settings import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'noticias.views.index', name='index'),
    url(r'^multimedia/$', 'noticias.views.multimedia', name='multimedia'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^noticias/', include('noticias.urls')),
    url(r'^eventos/', include('eventos.urls')),
    url(r'^biblioteca/', include('publicaciones.urls')),
    url(r'^multimedias/', include('multimedia.urls')),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    url('^pages/', include('django.contrib.flatpages.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^search/', include('googlesearch.urls')),
    url(r'^contactenos/$', 'noticias.views.contacto', name='contactenos'),
    url(r'^contacto_ajax/$', 'noticias.views.contacto_ajax', name='contacto_ajax'),
    url(r'^captcha/', include('captcha.urls')),
    
)


urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )