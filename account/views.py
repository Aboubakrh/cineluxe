from django.views.generic import TemplateView

from film_manager.models import Film


# Create your views here.

class AccueilView(TemplateView):
    template_name = 'accueil/accueil.html'

    def get_context_data(self, **kwargs):
        context = super(AccueilView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['films'] = Film.objects.filter(titre__icontains=query)
        else:
            context['films'] = Film.objects.all()[:4]
        return context