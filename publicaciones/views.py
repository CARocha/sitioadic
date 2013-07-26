from django.shortcuts import render, get_object_or_404
from .models import Publicaciones
from tagging.models import Tag, TaggedItem
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def filtro_publicaciones(request,categoria1,categoria2,template='publicaciones/publicaciones_list.html'):
    try:
        tag1 = Tag.objects.get(name=categoria1)
    except:
        tag1 = ''
    try:
        tag2 = Tag.objects.get(name=categoria2)
    except:
        tag2 = ''
    object_list = TaggedItem.objects.get_union_by_model(Publicaciones, [tag1,tag2])
    return render(request, template, {'object_list':object_list})
