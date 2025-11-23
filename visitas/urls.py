# visitas/urls.py
from django.urls import path
from . import views

app_name = 'visitas'

urlpatterns = [
    path('', views.VisitaListView.as_view(), name='lista_visitas'),
    path('visita/nueva/', views.VisitaCreateView.as_view(), name='crear_visita'),
    path('visita/<int:pk>/', views.VisitaDetailView.as_view(), name='detalle_visita'),
    path('visita/<int:pk>/editar/', views.VisitaUpdateView.as_view(), name='editar_visita'),
    path('visita/<int:pk>/borrar/', views.VisitaDeleteView.as_view(), name='borrar_visita'),

    # Checklist (crear / editar / borrar) — usamos funciones para insertar visita_id
    path('visita/<int:visita_id>/checklist/nuevo/', views.checklist_create, name='checklist_crear'),
    path('checklist/<int:pk>/editar/', views.checklist_edit, name='checklist_editar'),
    path('checklist/<int:pk>/borrar/', views.checklist_delete, name='checklist_borrar'),
]
