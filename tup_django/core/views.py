from django.views.generic.base import TemplateView

class IndexTemplateView(TemplateView): #LoginRequiredMixin will always redirect us to login url when not logged in
    template_name = 'index.html'