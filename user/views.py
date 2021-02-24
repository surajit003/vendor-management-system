from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView
from .models import CustomUser


class ProfileDetailView(UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = 'user/profile.html'
    slug_field = 'profile_id'
    slug_url_kwarg = 'profile_id'

    def test_func(self):
        return self.request.user.can_view(self.get_object())
