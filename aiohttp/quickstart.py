from aiohttp import web
routes = web.RouteTableDef()

@routes.get('/')
async def hello_handler(request):
    return web.Response(text="hello_handler")
@routes.get('/login')
async def signin_handler(request):
    return web.Response(text="signin_handler")
@routes.get('/add')
async def add_handler(request):
    return web.Response(text='add_handler')

app = web.Application()
app.add_routes([web.route("*",'/add', add_handler)]) # 添加路由表
web.run_app(app)

