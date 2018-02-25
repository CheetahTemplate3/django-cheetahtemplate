Django-CheetahTemplate
======================

Django-CheetahTemplate is a Django template backend to use
CheetahTemplate3_ in Django.

.. _CheetahTemplate3: http://cheetahtemplate.org/

It works with Python 2.7 or Python 3.4+, Django 1.11 and 2+,
CheetahTemplate3.

Install ``django-cheetahtemplate``. Add or change TEMPLATES in
``settings.py`` the following way:

.. code-block:: python

    TEMPLATES = [
        {
            'APP_DIRS': True,
            'BACKEND': 'django_cheetahtemplate.DjangoCheetahTemplate',
            'DIRS': [
            ],
            'OPTIONS': {
            },
        },
    ]

Put templates in ``cheetahtemplate`` subdirectories of installed
applications. See
`example <https://github.com/CheetahTemplate3/django-cheetahtemplate/tree/master/example>`_.

Author: Oleg Broytman <phd@phdru.name>.

Copyright (C) 2018 PhiloSoft Design.

License: MIT.

| Home Page:     https://github.com/CheetahTemplate3/django-cheetahtemplate
| PyPI:          https://pypi.python.org/pypi/django-cheetahtemplate
