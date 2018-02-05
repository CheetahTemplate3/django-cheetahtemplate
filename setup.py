#!/usr/bin/env python

try:
    from setuptools import setup
    is_setuptools = True
except ImportError:
    from distutils.core import setup
    is_setuptools = False

kw = {}
if is_setuptools:
    kw['install_requires'] = [
        "Django >1.11, <2; python_version=='2.7'",
        "Django >=2; python_version>='3.4'",
        "Cheetah3",
    ]

    kw['python_requires'] = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

setup(name='django-cheetahtemplate',
      version='0.3.0',
      description='Use CheetahTemplate3 in Django',
      long_description=open('README.rst', 'rU').read(),
      author='Oleg Broytman',
      author_email='phd@phdru.name',
      url='https://github.com/CheetahTemplate3/django-cheetahtemplate',
      license='MIT',
      platforms='Any',
      keywords=["cheetah", "django", "template"],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Text Processing',
      ],
      packages=['django_cheetahtemplate'],
      requires=['Django', 'Cheetah3'],
      **kw
      )
