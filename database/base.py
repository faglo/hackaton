from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from configs.vars import DATABASE_URL


engine = create_engine(DATABASE_URL, echo=True,
                       future=True, pool_size=25,  max_overflow=15)
Base = declarative_base(bind=engine)
