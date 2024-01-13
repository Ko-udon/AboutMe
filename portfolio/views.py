from django.views.generic import TemplateView
from .models import PageView

class IndexView(TemplateView):
    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['view_count'] = PageView.objects.get(name='index').view_count
    #     return context