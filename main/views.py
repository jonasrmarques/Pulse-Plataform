from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = "main/home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("principal-page")
        return super().dispatch(request, *args, **kwargs)
    
class PrincipalPageView(LoginRequiredMixin, TemplateView):
    template_name = "main/principalpage.html"
    
