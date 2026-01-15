from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "main/home.html"
    
class PrincipalPageView(TemplateView):
    template_name = "main/principalpage.html"