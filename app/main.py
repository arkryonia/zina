from app.core.config import settings

from app.apis.users import users

app = settings.init_app()

app.include_router(users.route)

@app.get('/', tags=["Index"])
def index():
    return {"DB": settings.get_db_uri()}
