from django.contrib import admin
from .models import Visita, Checklist

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'supervisor', 'zona', 'estado')
    search_fields = ('supervisor', 'zona')
    list_filter = ('estado', 'fecha')


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'visita', 'item', 'cumplido', 'nivel_riesgo')
    search_fields = ('item',)
    list_filter = ('nivel_riesgo', 'cumplido')
