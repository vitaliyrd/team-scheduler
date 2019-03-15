# Package meta-data.
import io
import os

from setuptools import setup, find_packages

NAME = 'team-scheduler'
DESCRIPTION = 'Scheduling tool for teams.'
URL = 'https://github.com/vitaliyrd/team-scheduler'
EMAIL = 'vitaliyrd@gmail.com'
AUTHOR = 'Vitaliy Radchishin'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '1.0.0'

REQUIRED = [
    # Required package dependencies.
    'Babel',
    'Django',
    'pytz',
]

EXTRAS = [
    # Optional package dependencies.
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
)
