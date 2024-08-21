from django.views import generic as views

from petstagram.common.view_mixins import RedirectToDashBoard
from petstagram.main.models import PetPhoto


class HomeView(RedirectToDashBoard, views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True,
        return context


class DashBoardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'
