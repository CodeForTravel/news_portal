from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from django.views.generic import View


# views for non logged in user
class IndexView(TemplateView, View):
    template_name = "base/index.html"
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# views for logged in user
class AuthenticatedIndexView(TemplateView, View):
    template_name = "base/authenticated_index.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)