from django.views.generic import TemplateView
from .models import  category, items


class homeview(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = category.objects.all()[:5]
        context["best"] = items.objects.filter(Best_Sellers=True)[:8]
        context["new"] = items.objects.filter(New_Arrivals=True).order_by('-id')[:3]
        context["feat"] = items.objects.filter(Featured_Products=True)[:8]
        return context
