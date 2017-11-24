from ideatank import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship


class Idea(db.Model):
    """Idea
    This class defines the data for an idea
    """
    __tablename__ = 'ideas'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    author = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.cat_id', name='fk_cat_id',
                                          onupdate='cascade', ondelete='RESTRICT'), nullable=False)
    category = relationship("Category", passive_deletes=True, passive_updates=True)
    created_at = Column(DateTime)

    def __repr__(self):
        return 'User <{}>'.format(self.__dict__)

class Category(db.Model):
    """Category
    Provide seed data for categories
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    def __repr__(self):
        return 'Category <{}>'.format(self.name)


class User(db.Model):
    """
    User
    Provide seed data for users
    """
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    fname = Column(String(40), nullable=False)
    lname = Column(String(40), nullable=False)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(42), nullable=False)
    email = Column(String(60), unique=True)
