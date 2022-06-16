from django import forms
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.edit import FormView

from main.models import Expert


class ExpertForm(forms.Form):
    text = forms.CharField(help_text="Введите фразу для поиска")


class ExpertFormView(FormView):
    template_name = 'index.html'
    form_class = ExpertForm
    success_url = ''

    def form_valid(self, form):
        text = form.data.get("text", "")
        experts = Expert.objects.order_by("id").filter(
            Q(text__icontains=text) |
            Q(help__icontains=text) |
            Q(expertise__icontains=text) |
            Q(competencies__icontains=text)
        )

        return render(self.request, self.template_name, {"experts": experts})
