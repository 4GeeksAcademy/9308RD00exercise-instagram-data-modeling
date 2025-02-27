import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()






class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)



class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_it = Column(Integer, ForeignKey('user.id')) 
    second_user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)





class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



class Comment(Base):
    __tablename__ = 'comment'
    id = id = Column(Integer, primary_key=True)
    comment = Column(String(500))
    author_id = Column(Integer, ForeignKey ('user.id'))
    post_id = Column(Integer, ForeignKey ('post.id'))
    user = relationship(User)
    post = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    id = id = Column(Integer, primary_key=True)
    type = Column() 
    url = Column(String(), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)




    def to_dict(self):
        return {}






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
