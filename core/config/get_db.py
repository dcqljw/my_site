from database import SessionLocal


def get_db():
    local = SessionLocal()
    try:
        yield local
    finally:
        local.close()
