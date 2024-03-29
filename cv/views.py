from django.views.generic import ListView
import datetime

# Create your views here.
class AccueilView(ListView):
    """ That class to get the acceuil page"""
    template_name = "cv/accueil.html"

    def get_queryset(self):
        # in 24 february 2021 458 day in the site duolingo
        first_day = datetime.date(2021, 2, 24)
        today = datetime.date.today() 
        diff = first_day - today
        self.day = 550
        return self.day

    def get_context_data(self, **kwargs):
        kwargs['day'] = self.day
        return super(AccueilView, self).get_context_data(**kwargs)