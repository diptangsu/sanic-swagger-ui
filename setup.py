import pathlib
from setuptools import setup
from sanic_swagger_ui import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='sanic-swagger-ui',
    version=__version__,
    description='Swagger UI blueprint for Sanic',
    long_description=README,
    long_description_content_type='text/markdown',
    zip_safe=False,

    url='https://github.com/diptangsu/sanic-swagger-ui',

    author='Diptangsu Goswami',
    author_email='diptangsu.97@gmail.com',
    license='MIT',

    classifiers=[
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
