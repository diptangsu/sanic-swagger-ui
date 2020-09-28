import os
import json
import inspect
from sanic import Blueprint, response
from jinja2 import Environment, PackageLoader


def get_swaggerui_blueprint(
        base_url,
        api_url,
        blueprint_name='swagger_ui',
        url_prefix='/swagger',
        config=None,
    ):
    env = Environment(loader=PackageLoader('sanic_swagger_ui', 'templates'))

    swagger_ui = Blueprint(blueprint_name, url_prefix=url_prefix)
    swagger_ui.static('/static', './static')

    print('*' * 50)
    print(os.getcwd())
    print(os.listdir())
    print(__file__)
    print(inspect.getfile(inspect.currentframe()))
    print('*' * 50)

    template = env.get_template('index.html')

    default_config = {
        'app_name': 'Swagger UI',
        'dom_id': '#swagger-ui',
        'url': api_url,
        'layout': 'StandaloneLayout',
        'deepLinking': True
    }
    if config:
        default_config.update(config)

    fields = {
        # Some fields are used directly in template
        'base_url': base_url + '/static',
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


if __name__ == '__main__':
    from sanic import Sanic

    app = Sanic(__name__)

    SWAGGER_URL = '/swagger'
    API_URL = '/swagger/dist/index.yaml' 

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL
    )
    app.blueprint(swaggerui_blueprint)

    @app.route("/")
    async def test(req):
        return response.text('Hello World from Sanic', status=200)

    app.run(debug=True, host='0.0.0.0', port=5555)
