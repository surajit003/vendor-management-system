from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = "user"

urlpatterns = [
    url(
        r"^profile/(?P<profile_id>[0-9a-f-]+)/$",
        login_required(views.ProfileDetailView.as_view()),
        name="profile_detail",
    ),
    ]