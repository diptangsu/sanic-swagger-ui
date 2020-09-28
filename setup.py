from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sanic-swagger-ui',
    version='0.0.1',
    description='Swagger UI blueprint for Sanic',
    long_description=long_description,
    zip_safe=False,

    url='',

    author='Diptangsu Goswami',
    author_email='diptangsu.97@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='sanic swagger',
    packages=['sanic_swagger_ui'],
    install_requires=['sanic', 'jinja2'],
    package_data={
        'sanic_swagger_ui': [
            'LICENSE',
            'README.md',
            'templates/*.html',
            'static/VERSION',
            'static/LICENSE',
            'static/README.md',
            'static/*.html',
            'static/*.js',
            'static/*.css',
            'static/*.png'
        ],
    }
)
