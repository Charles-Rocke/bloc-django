
from django.views.generic import TemplateView
#from webauthn import registration

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    

    
    