from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "index.tmpl"

    def get_context_data(self, name=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['name'] = name or 'Test'
        return context

    def get(self, request, name=None):
        context = self.get_context_data(name=name)
        return self.render_to_response(context)


class SimpleView(IndexView):
    template_name = "simple/index.tmpl"
