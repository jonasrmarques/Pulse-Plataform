from django.views.generic import TemplateView


class UsersPageView(TemplateView):
    template_name = "users/users.html"