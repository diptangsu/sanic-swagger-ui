import json
import inspect
import sysconfig
from sanic import Blueprint, response
from jinja2 import Environment, PackageLoader


def get_swaggerui_blueprint(
        docs_path,
        url_prefix='/swagger',
        app_name='Swagger UI',
        blueprint_name='swagger_ui',
        config=None,
    ):
    env = Environment(loader=PackageLoader('sanic_swagger_ui', 'templates'))

    swagger_ui = Blueprint(blueprint_name, url_prefix=url_prefix)
    site_packages_path = sysconfig.get_paths()["purelib"]
    static_path = site_packages_path + '/sanic_swagger_ui/static'
    swagger_ui.static('/static', static_path)

    template = env.get_template('index.html')

    default_config = {
        'app_name': app_name,
        'dom_id': '#swagger-ui',
        'url': docs_path,
        'layout': 'StandaloneLayout',
        'deepLinking': True
    }
    if config:
        default_config.update(config)

    fields = {
        # Some fields are used directly in template
        'base_url': url_prefix + '/static',
        'app_name': default_config.pop('app_name'),
        # Rest are just serialized into json string for inclusion in the .js file
        'config_json': json.dumps(default_config),
    }

    @swagger_ui.route('/docs')
    @swagger_ui.route('/docs/<path:path>')
    def show(request, path=None):
        if not path or path == 'index.html':
            content = template.render(**fields)
            return response.html(content)

    return swagger_ui
