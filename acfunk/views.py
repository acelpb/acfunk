from django.views.generic import TemplateView

from artwork.models import Artwork


class HomeView(TemplateView):
    template_name = 'acfunk/home.html'


class EtudesView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.ETUDE).all()
        }


class PaintingsView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.PAINTING).all()
        }


class SketchesView(TemplateView):
    template_name = 'acfunk/gallery.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'gallery': Artwork.objects.filter(type=Artwork.SKETCH).all()
        }


class AboutView(TemplateView):
    template_name = 'acfunk/about.html'


class ContactView(TemplateView):
    template_name = 'acfunk/contact.html'
