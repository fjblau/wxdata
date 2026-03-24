from arango import ArangoClient
from app.config import settings


def get_db():
    client = ArangoClient(hosts=settings.arango_host)
    db = client.db(
        settings.arango_db,
        username=settings.arango_user,
        password=settings.arango_password,
    )
    return db
