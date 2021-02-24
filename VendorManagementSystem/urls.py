from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
app_name = "vendor"
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^__debug__/", include(debug_toolbar.urls)),
    url(r"^accounts/", include("allauth.urls")),
    url(r"^catalog/", include("catalog.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Vendor Admin"
admin.site.site_title = "Vendor Admin Portal"
admin.site.index_title = "Welcome to Vendor Admin Portal"

