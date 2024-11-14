"""
URL configuration for Example project.
"""

from django.apps import apps
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from exemple.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Indique au serveur de dev de service les fichiers statiques et media
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    # Add django-pattern-library urls
    if apps.is_installed("pattern_library"):
        urlpatterns += [
            path("patterns/", include("pattern_library.urls")),
        ]

    if apps.is_installed("django_browser_reload"):
        urlpatterns += [
            path("__reload__/", include("django_browser_reload.urls")),
        ]
