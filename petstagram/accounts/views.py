from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from petstagram.accounts.forms import ProfileForm
from petstagram.accounts.models import Profile
from petstagram.common.view_mixins import RedirectToDashBoard
from petstagram.main.models import Pet, PetPhoto
from django.views import generic as views


class UserRegisterView(RedirectToDashBoard, views.CreateView):
    form_class = ProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView:
    pass


class EditProfileView:
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_id=self.object.user_id))

        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pet_photos_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })

        return context
