#this(every model) will represents a table in the database
#Normally, when you interact with a database, you work with tables (collections of data) and rows (each individual data record). 
# In SQLAlchemy, instead of writing raw SQL code for tables, you use classes in Python to represent tables.
#The declarative base is the base class you need to create these table-representing classes.

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Post(Base):  #this is SQL_ALchemy model(or ORM Model) it is responsible for defining, quering, creating, deleting and updating table in database 
    __tablename__= "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published =Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"), nullable= False)

    owner = relationship("User") #it will help to create a relationship with other class, so that you can extract information from the other class

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable= False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))

class Vote(Base):
    __tablename__ ="votes"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)


