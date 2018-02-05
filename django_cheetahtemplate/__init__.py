"""
django-cheetahtemplate
"""

from imp import load_source
import os
import py_compile

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
        options = params.pop('OPTIONS')
        self.cacheModule = options.get('cacheModule')
        super(DjangoCheetahTemplate, self).__init__(params)

    def from_string(self, template_code):
        try:
            return CheetahTemplate(Template.compile(source=template_code))
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
        generated_template = os.path.join(template_dirname,
                                          template_name_base + '.py')
        if os.path.exists(generated_template) and \
                (os.path.getmtime(generated_template) >=
                 os.path.getmtime(template_full_path)):
            template_mod = load_source(template_name_base, generated_template)
            return CheetahTemplate(getattr(template_mod, template_name_base))
        try:
            templateClass = Template.compile(
                file=template_full_path,
                moduleName=template_name_base,
            )
        except IOError as exc:
            raise TemplateDoesNotExist(exc.args, backend=self)
        except ParseError as exc:
            raise TemplateSyntaxError(exc.args)
        else:
            if not self.cacheModule:
                return CheetahTemplate(templateClass)
            try:
                with open(generated_template, 'wt') as pyfile:
                    pyfile.write(templateClass().generatedModuleCode())
            except IOError:  # Write failed - ignore the error
                return CheetahTemplate(templateClass)
            else:
                py_compile.compile(generated_template)
                template_mod = load_source(
                    template_name_base, generated_template)
                return CheetahTemplate(
                    getattr(template_mod, template_name_base))


class CheetahTemplate(object):

    def __init__(self, templateClass):
        self.templateClass = templateClass

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        template = self.templateClass(searchList=[context])
        return template.respond()
