"""install ID"""
from functools import lru_cache
from uuid import uuid4

from psycopg2 import connect

from authentik.lib.config import CONFIG


@lru_cache
def get_install_id() -> str:
    """Get install ID of this instance. The method is cached as the install ID is
    not expected to change"""
    from django.conf import settings
    from django.db import connection

    if settings.TEST:
        return str(uuid4())
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM authentik_install_id LIMIT 1;")
        return cursor.fetchone()[0]


@lru_cache
def get_install_id_raw():
    """Get install_id without django loaded, this is required for the startup when we get
    the install_id but django isn't loaded yet and we can't use the function above."""
    conn = connect(
        dbname=CONFIG.y("postgresql.name"),
        user=CONFIG.y("postgresql.user"),
        password=CONFIG.y("postgresql.password"),
        host=CONFIG.y("postgresql.host"),
        port=int(CONFIG.y("postgresql.port")),
        sslmode=CONFIG.y("postgresql.sslmode"),
        sslrootcert=CONFIG.y("postgresql.sslrootcert"),
        sslcert=CONFIG.y("postgresql.sslcert"),
        sslkey=CONFIG.y("postgresql.sslkey"),
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM authentik_install_id LIMIT 1;")
    return cursor.fetchone()[0]
