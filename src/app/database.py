from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.app.utils.config import db_settings

# DATABASE URL ACCESS CREDENTIALS
POSTGRES_URI = f"postgresql://{db_settings.db_username}:{db_settings.db_password}@{db_settings.db_host}:{db_settings.db_port}/{db_settings.db_name}"


engine = create_engine(POSTGRES_URI)

# DATABASE SESSION INSTANCE
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# DATABASE CLASS THAT IS USED TO SET UP DATABASE TABLE
Base = declarative_base()


print("Database Layer is ready!")
