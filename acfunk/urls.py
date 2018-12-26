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
from django.contrib import admin
# sitemaps.py
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.urls import reverse
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import AboutView
from .views import ContactView
from .views import EtudesView
from .views import HomeView
from .views import PaintingsView
from .views import SketchesView


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'paintings', 'etudes', 'sketches', 'about', 'contact']

    def location(self, item):
        return reverse(item)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('paintings/', PaintingsView.as_view(), name='paintings'),
    path('etudes/', EtudesView.as_view(), name='etudes'),
    path('sketches/', SketchesView.as_view(), name='sketches'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap, }},
         name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
