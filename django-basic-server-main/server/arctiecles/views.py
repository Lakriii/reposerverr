from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Arctiecle

class ArctiecleListView(ListView):
    model = Arctiecle
    context_object_name = "arctiecles"
    template_name = "arctiecles/arctiecles_list.html"
    paginate_by = 10  # voliteľné


class ArctiecleDetailView(DetailView):
    model = Arctiecle
    context_object_name = "arctiecle"
    template_name = "arctiecles/arctiecles_detail.html"


class ArctiecleCreateView(LoginRequiredMixin, CreateView):
    model = Arctiecle
    fields = ["title", "content"]
    template_name = "arctiecles/arctiecles_form.html"
    success_url = reverse_lazy("arctiecle-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArctiecleUpdateView(LoginRequiredMixin, UpdateView):
    model = Arctiecle
    fields = ["title", "content"]
    template_name = "arctiecles/arctiecles_form.html"
    success_url = reverse_lazy("arctiecle-list")

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return qs
        return qs.filter(author=self.request.user)


class ArctiecleDeleteView(LoginRequiredMixin, DeleteView):
    model = Arctiecle
    context_object_name = "arctiecle"
    template_name = "arctiecles/arctiecles_confirm_delete.html"
    success_url = reverse_lazy("arctiecle-list")

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return qs
        return qs.filter(author=self.request.user)