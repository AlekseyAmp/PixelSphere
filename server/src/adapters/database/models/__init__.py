import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base, declared_attr


metadata = sa.MetaData()
Base = declarative_base(metadata=metadata)