from app.core.config import settings

app = settings.init_app()


@app.get('/', tags=["Index"])
def index():
    return {"DB": settings.get_db_uri()}
