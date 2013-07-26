from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from .models import Publicaciones

urlpatterns = patterns('publicaciones.views',
    url(r'^lista/$',  ListView.as_view(model=Publicaciones,
                                       queryset=Publicaciones.objects.all(),
                                       paginate_by=5), 
                                       name='publicaciones_lista'),
    
    url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Publicaciones,
                                                    queryset=Publicaciones.objects.all(),
                                                    ), 
                                                    name='publicaciones_detalles'),
    url(r'^categoria/(?P<categoria1>[-_\w]+)/(?P<categoria2>[-_\w]+)/$','filtro_publicaciones', 
                                                                name='filtro_publicaciones'),
    )