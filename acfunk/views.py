from django.views.generic import TemplateView

from artwork.models import Artwork


class HomeView(TemplateView):
    template_name = 'acfunk/home.html'


class AbstractsView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.ABSTRACTS).order_by('order').all(),
            'title': Artwork.TYPE_CHOICES[Artwork.ABSTRACTS][1],
        }


class ImpressionsView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.IMPRESSIONS).order_by('order').all(),
            'title': Artwork.TYPE_CHOICES[Artwork.IMPRESSIONS][1],
        }


class BirdsView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.BIRDS).order_by('order').all(),
            'title': Artwork.TYPE_CHOICES[Artwork.BIRDS][1],
        }


class PortraitsView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.PORTRAITS).order_by('order').all(),
            'title': Artwork.TYPE_CHOICES[Artwork.PORTRAITS][1],
        }


class AboutView(TemplateView):
    template_name = 'acfunk/about.html'


class ContactView(TemplateView):
    template_name = 'acfunk/contact.html'
