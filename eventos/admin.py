from django.contrib import admin
from .models import Eventos
from multimedia.models import *

class FotosAdmin(generic.GenericTabularInline):
    model = Fotos
    extra = 1

class AdjuntosAdmin(generic.GenericTabularInline):
    model = Adjuntos
    extra = 1

class EventosAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        elif request.user.is_staff:
            return self.model.objects.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.autor = request.user
        instance.save()
        return instance

    exclude = ['autor']
    inlines = [FotosAdmin, AdjuntosAdmin]
    list_display = ['titulo','fecha_inicio','fecha_finalizacion','autor']
    search_fields = ['titulo',]
    date_hierarchy = 'fecha_inicio'

admin.site.register(Eventos, EventosAdmin)