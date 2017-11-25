from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Table
from sqlalchemy.orm import relationship, backref

from werkzeug.security import generate_password_hash

from datetime import datetime

from ideatank import db


class Idea(db.Model):
    """Idea
    This class defines the data for an idea
    """
    __tablename__ = 'ideas'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    author = relationship('User')
    user_id = Column(Integer, ForeignKey('users.id', name='fk_user_id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', name='fk_cat_id',
                                          onupdate='cascade', ondelete='RESTRICT'), nullable=False)
    category = relationship('Category', passive_deletes=True, passive_updates=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    tags = relationship('Tag', backref=backref('ideas', lazy='dynamic'), secondary='idea_tag')

    def __repr__(self):
        return 'Idea <{}>'.format(self.__dict__)


class Category(db.Model):
    """Category
    Provide seed data for categories
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    
    def __repr__(self):
        return 'Category <{}>'.format(self.name)


class User(db.Model):
    """
    User
    Provide seed data for users
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(40), nullable=False)
    lastname = Column(String(40), nullable=False)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(60), unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return 'User <{}>'.format(self.__dict__)


class Tag(db.Model):
    """Tag
    Tag model definition
    """
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    created_at = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return 'Tag <{}>'.format(self.__dict__)


class IdeaTagAssociation(db.Model):
    """Association
    Pivot table for idea and tag relations
    """
    __tablename__ = 'idea_tag'

    idea_id = Column(Integer, ForeignKey('ideas.id', ondelete='CASCADE'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True)
    idea = relationship('Idea', backref='ideas')
    tag = relationship('Tag', backref='tags')


if __name__ == '__main__':
    db.create_all()
