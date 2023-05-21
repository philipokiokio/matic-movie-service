from src.app.database import SessionLocal


# DATABASE SESSION CONTEXT {CONTROLS ACCESS TO THE DB}
def get_db():
    # SESSION INTIALIZED
    db = SessionLocal()

    try:
        yield db
    finally:
        # CLOSE DB ACCESS
        db.close()
