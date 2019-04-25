"""acfunk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# sitemaps.py
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.urls import reverse

from .views import AboutView, AbstractsView, ImpressionsView, BirdsView, PortraitsView
from .views import ContactView
from .views import HomeView


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'paintings', 'etudes', 'sketches', 'about', 'contact']

    def location(self, item):
        return reverse(item)


urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('abstracts/', AbstractsView.as_view(), name='abstracts'),
                  path('impressions/', ImpressionsView.as_view(), name='impressions'),
                  path('birds/', BirdsView.as_view(), name='birds'),
                  path('portraits/', PortraitsView.as_view(), name='portraits'),
                  path('about/', AboutView.as_view(), name='about'),
                  path('contact/', ContactView.as_view(), name='contact'),
                  path('admin/', admin.site.urls),
                  path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap, }},
                       name='django.contrib.sitemaps.views.sitemap')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
