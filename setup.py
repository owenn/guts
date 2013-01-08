
from distutils.core import setup

setup(
    name    = 'guts',
    version = '0.1',
    description = 'Lightweight declarative YAML and XML data binding for Python.',
    package_dir = { '': 'src' },
    py_modules = ['guts'],
    scripts = [ 'scripts/xmlschema-to-guts' ],
    author = 'Sebastian Heimann',
    author_email = 'sebastian.heimann@gfz-potsdam.de',
    url = 'http://emolch.github.com/guts/',
)
