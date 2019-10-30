from django.conf import settings
from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin

from welcome.views import index, health

app_name="CyNest Django"

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name="index"),
    url(r'^health$', health),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
