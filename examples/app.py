from sanic import Sanic
from sanic import response
from sanic_swagger_ui import get_swaggerui_blueprint

app = Sanic(__name__)
STATIC_URL = '/static'
app.static(STATIC_URL, './static')  # set static dir path

SWAGGER_URL = '/swagger'
DOCS_PATH = STATIC_URL + '/swagger/index.yaml'  # serves files from the static dir

swaggerui_blueprint = get_swaggerui_blueprint(
    DOCS_PATH,
    SWAGGER_URL,
    app_name='Swagger BP Test'
)
app.blueprint(swaggerui_blueprint)


@app.route('/')
async def index(req):
    return response.html((
        'Hello World from Sanic'
        '<br>'
        'Click <a href="/swagger/docs">here</a> to view swagger docs'), 
        status=200
    )


if __name__ == '__main__':
    app.run(debug=True)