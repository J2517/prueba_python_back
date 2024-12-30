from app.routers.user_routes import router as user_routes

def incluide_routes(app):
    app.include_router(user_routes)
    