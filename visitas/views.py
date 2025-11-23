from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Visita, Checklist
from .forms import VisitaForm, ChecklistForm

# Create your views here.

# visitas/views.py

class VisitaListView(LoginRequiredMixin, ListView):
    model = Visita
    template_name = "visitas/visita_list.html"
    context_object_name = "visitas"
    paginate_by = 10
    ordering = ['-fecha']

class VisitaDetailView(LoginRequiredMixin, DetailView):
    model = Visita
    template_name = "visitas/visita_detail.html"
    context_object_name = "visita"

class VisitaCreateView(LoginRequiredMixin, CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = "visitas/visita_form.html"

    def get_success_url(self):
        messages.success(self.request, "Visita creada correctamente.")
        return reverse('visitas:detalle_visita', kwargs={'pk': self.object.pk})

class VisitaUpdateView(LoginRequiredMixin, UpdateView):
    model = Visita
    form_class = VisitaForm
    template_name = "visitas/visita_form.html"

    def get_success_url(self):
        messages.success(self.request, "Visita actualizada.")
        return reverse('visitas:detalle_visita', kwargs={'pk': self.object.pk})

class VisitaDeleteView(LoginRequiredMixin, DeleteView):
    model = Visita
    template_name = "visitas/visita_confirm_delete.html"
    success_url = reverse_lazy('visitas:lista_visitas')

@login_required
def checklist_create(request, visita_id):
    visita = get_object_or_404(Visita, pk=visita_id)
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.visita = visita
            checklist.save()
            messages.success(request, "Item de checklist añadido.")
            return redirect('visitas:detalle_visita', pk=visita.pk)
    else:
        form = ChecklistForm()
    return render(request, 'visitas/checklist_form.html', {'form': form, 'visita': visita})

@login_required
def checklist_edit(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    if request.method == 'POST':
        form = ChecklistForm(request.POST, instance=checklist)
        if form.is_valid():
            form.save()
            messages.success(request, "Checklist actualizado.")
            return redirect('visitas:detalle_visita', pk=checklist.visita.pk)
    else:
        form = ChecklistForm(instance=checklist)
    return render(request, 'visitas/checklist_form.html', {'form': form, 'visita': checklist.visita})

@login_required
def checklist_delete(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    visita_pk = checklist.visita.pk
    if request.method == 'POST':
        checklist.delete()
        messages.success(request, "Checklist eliminado.")
        return redirect('visitas:detalle_visita', pk=visita_pk)
    return render(request, 'visitas/checklist_confirm_delete.html', {'checklist': checklist})
