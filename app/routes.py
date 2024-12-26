from app.routers.test_routes import router as test_routes
from app.routers.user_routes import router as user_routes


def incluide_routes(app):
    prefix = "/api/v1"
    app.include_router(test_routes, prefix=prefix)
    app.include_router(user_routes)
    