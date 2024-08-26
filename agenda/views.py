from django.views.generic import CreateView, ListView, DeleteView   
from .models import Cita
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError, transaction
from roll.models import TipoUsuario


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(self.request, "¡Usted no tiene autorización!")
        return redirect("index")
    
class ClienteCreateMixin(LoginRequiredMixin):
    login_url = 'signin'

    def handle_no_permission(self):
        messages.error(self.request, "¡Debe iniciar sesión para agendar una hora!")
        return redirect("signin")    

# Vistas
class CitaCreateView(ClienteCreateMixin, CreateView):
    model = Cita
    template_name = 'agendar_hora.html'
    fields = ['veterinario', 'fecha_cita', 'sucursal', 'horario']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            with transaction.atomic():
                response = super().form_valid(form)
                return response
        except IntegrityError:
            form.add_error(None, "Ya existe una cita para este veterinario en esta fecha y horario.")
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_usuario = None
        if self.request.user.is_authenticated:
            try:
                tipo_usuario = TipoUsuario.objects.get(usuario=self.request.user)
            except TipoUsuario.DoesNotExist:
                pass
        context['tipo_usuario'] = tipo_usuario.tipo if tipo_usuario else None
        return context    

class CitaListView(ClienteCreateMixin, TestMixinIsAdmin, ListView):
    template_name = 'lista_citas.html'

    def get_queryset(self):
        return Cita.objects.all().order_by('-pk')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_usuario = None
        if self.request.user.is_authenticated:
            try:
                tipo_usuario = TipoUsuario.objects.get(usuario=self.request.user)
            except TipoUsuario.DoesNotExist:
                pass
        context['tipo_usuario'] = tipo_usuario.tipo if tipo_usuario else None

        # Agregar especialidad del veterinario y sucursal
        citas = self.get_queryset()
        for cita in citas:
            cita.especialidad = cita.veterinario.especialidad
            cita.sucursal = cita.sucursal

        context['citas'] = citas
        return context   
    

class CitaDeleteView(TestMixinIsAdmin, ClienteCreateMixin, DeleteView):
    model = Cita
    success_url = reverse_lazy('lista_citas')
    template_name = 'eliminar_cita.html'

    def get_success_url(self):
        messages.success(self.request, "Cita cancelada con éxito!")
        return reverse_lazy('lista_citas')

    def delete(self, request, *args, **kwargs):
        print("Entrando al método delete de CitaDeleteView")
        self.object = self.get_object()
        print(f"Cita a eliminar: {self.object}")
        success_url = self.get_success_url()
        print(f"URL de éxito: {success_url}")
        self.object.delete()
        print("Cita eliminada exitosamente")
        return redirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_usuario = None
        if self.request.user.is_authenticated:
            try:
                tipo_usuario = TipoUsuario.objects.get(usuario=self.request.user)
            except TipoUsuario.DoesNotExist:
                pass
        context['tipo_usuario'] = tipo_usuario.tipo if tipo_usuario else None
        return context  


cita_create = CitaCreateView.as_view()    
cita_list = CitaListView.as_view()
cita_delete = CitaDeleteView.as_view()