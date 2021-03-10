from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from products_data import products_data


templates = Jinja2Templates(directory='templates')

async def homepage(request):
    return templates.TemplateResponse('e_commerce.html', {'request': request})

async def products(request):
    return JSONResponse(products_data)

app = Starlette(debug=True, routes=[
    Route('/', homepage), 
    Route('/products', products), 
    Mount('/static', StaticFiles(directory='static'), name='static')
])

