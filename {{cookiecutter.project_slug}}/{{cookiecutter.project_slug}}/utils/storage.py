from urllib.parse import urljoin

from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage


class GCStaticStorage(GoogleCloudStorage):
    location = "static"

    def url(self, name):
        return urljoin(settings.STATIC_URL, name)


class GCMediaStorage(GoogleCloudStorage):
    location = "media"
    file_overwrite = False

    def url(self, name):
        return urljoin(settings.MEDIA_URL, name)
