"""
django-cheetahtemplate
"""

from imp import load_source
import os

from Cheetah.Parser import ParseError
from Cheetah.Template import Template

from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy


class DjangoCheetahTemplate(BaseEngine):

    # Name of the subdirectory containing the templates for this engine
    # inside an installed application.
    app_dirname = 'cheetahtemplate'

    def __init__(self, params):
        params = params.copy()
        del params['OPTIONS']
        super(DjangoCheetahTemplate, self).__init__(params)

    def from_string(self, template_code):
        try:
            return CheetahTemplate(Template(source=template_code))
        except ParseError as exc:
            raise TemplateSyntaxError(exc.args)

    def get_template(self, template_name):
        for template_full_path in self.iter_template_filenames(template_name):
            if os.path.exists(template_full_path):
                break
        else:
            raise TemplateDoesNotExist(template_name, backend=self)
        template_dirname = os.path.dirname(template_full_path)
        template_name_base = \
            os.path.splitext(os.path.basename(template_name))[0]
        compiled_template = os.path.join(template_dirname,
                                         template_name_base + '.py')
        if os.path.exists(compiled_template) and \
                (os.path.getmtime(compiled_template) >=
                 os.path.getmtime(template_full_path)):
            template_mod = load_source(template_name_base, compiled_template)
            return CheetahTemplate(getattr(template_mod, template_name_base))
        try:
            Template(file=template_full_path)
        except IOError as exc:
            raise TemplateDoesNotExist(exc.args, backend=self)
        except ParseError as exc:
            raise TemplateSyntaxError(exc.args)
        return CheetahTemplate(Template, template_full_path)


class CheetahTemplate(object):

    def __init__(self, template, source=None):
        self.template = template
        self.source = source

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        if self.source:
            template = self.template(file=self.source, searchList=[context])
        else:
            template = self.template(searchList=[context])
        return template.respond()
