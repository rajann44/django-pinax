from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('pinax.apps.account.urls')),
    url(r'^profiles/', include('pinax.apps.profiles.urls')),
    url(r'^notifications/', include('pinax.apps.notification.urls')),
    url(r'^messages/', include('pinax.apps.messages.urls')),
    url(r'^tribes/', include('pinax.apps.tribes.urls')),
    url(r'^photos/', include('pinax.apps.photos.urls')),
    url(r'^topics/', include('pinax.apps.topics.urls')),
    url(r'^wiki/', include('pinax.apps.wiki.urls')),
    url(r'^swaps/', include('pinax.apps.swaps.urls')),
    url(r'^ratings/', include('pinax.apps.ratings.urls')),
    url(r'^comments/', include('pinax.apps.threadedcomments.urls')),
    url(r'^relationships/', include('pinax.apps.relationships.urls')),
    url(r'^avatar/', include('pinax.apps.avatar.urls')),
    url(r'^tagging/', include('pinax.apps.tagging.urls')),
    url(r'^bookmarks/', include('pinax.apps.bookmarks.urls')),
    url(r'^activities/', include('pinax.apps.activities.urls')),
] 