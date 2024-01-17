from django.views.generic import TemplateView
from .models import PageView

class IndexView(TemplateView):
    template_name = "index.html"
    model = PageView

    # 조회수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pageView = PageView.objects.get(pk=1)
        pageView.view_count += 1
        pageView.save()
        context['view_count'] = pageView.view_count
        return context