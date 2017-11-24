from flask import Flask, session, render_template, redirect, request, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
# from models import User, Category, Idea

ideatank = Flask(__name__)
ideatank.secret_key = '842be30bd2a3f2fdcfcbaa93e6b5960dfdb3660971b91537'
ideatank.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/ideatank'
db = SQLAlchemy(ideatank)


@ideatank.route('/')
def home():
    context = {
        'title': 'Dashboard'
    }

    return render_template('index.html', **context)

@ideatank.route('/ideas')
def ideas():
    context = {
        'title': 'Ideas',
        'ideas': []
    }

    return render_template('ideas.html', **context)

@ideatank.route('/tags')
def tags():
    context = {
        'title': 'Tags',
        'tags': []
    }

    return render_template('tags.html', **context)

@ideatank.route('/categories')
def categories():
    context = {
        'title': 'Categories',
        'categories': []
    }

    return render_template('categories.html', **context)

@ideatank.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    flash('You have successfully logged out', category='success')
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    ideatank.run(debug=True, port=6060)
