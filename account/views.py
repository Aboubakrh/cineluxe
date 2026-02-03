from django.views.generic import TemplateView

from film_manager.models import Film


# Create your views here.

class AccueilView(TemplateView):
    template_name = 'accueil/accueil.html'

    def get_context_data(self, **kwargs):
        context = super(AccueilView, self).get_context_data(**kwargs)
        context['films'] = Film.objects.all()
        print(context['films'])
        return context