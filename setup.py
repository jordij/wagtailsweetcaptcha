import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtailsweetcaptcha',
    version='0.1.1',
    packages=['wagtailsweetcaptcha'],
    install_requires=['django-sweetcaptcha'],
    include_package_data=True,
    license='BSD License',
    description='A simple sweetcaptcha field for Wagtail Form Pages.',
    long_description=README,
    url='http://github.com/jordij/wagtailsweetcaptcha',
    author='Jordi J. Tablada',
    author_email='hi@jordijoan.me',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
