from sanic import Sanic
from sanic import response
from sanic_swagger_ui import get_swaggerui_blueprint

app = Sanic(__name__)
app.static('/static', './static')

SWAGGER_URL = '/swagger'
DOCS_PATH = '/static/swagger/index.yaml' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    DOCS_PATH,
    app_name='Swagger BP Test'
)
app.blueprint(swaggerui_blueprint)


@app.route("/")
async def test(req):
    return response.text('Hello World from Sanic', status=200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1200)
