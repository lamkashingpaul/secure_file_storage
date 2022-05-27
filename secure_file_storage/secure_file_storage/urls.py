from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from private_storage.views import PrivateStorageView


class StorageView(PrivateStorageView):
    def can_access_file(self, private_file):
        # check if user is logged in and has access to file with user id
        return int(private_file.relative_name.split('/')[0]) == self.request.user.id


urlpatterns = [
    re_path('^private-media/', include([re_path(r'^(?P<path>.*)$', StorageView.as_view(), name='serve_private_file')])),

    path('', include('files.urls')),

    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

    urlpatterns += path('admin/', admin.site.urls),
