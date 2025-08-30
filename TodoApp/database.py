from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:pagal@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = "postgresql://chanky:Number12345@apppostgresql.postgres.database.azure.com:5432/TodoApplicationDatabase?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()