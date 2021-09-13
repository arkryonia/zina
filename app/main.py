from app.core.config import settings

app = settings.init_app()


@app.get('/')
def index():
    return {"DB": settings.DB_URL}
