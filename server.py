from flask import render_template, redirect, url_for, session, flash, request

from ideatank import app, db, hash_password
from models import User, Idea, Tag, Category

@app.route('/')
def home():
    context = {
        'title': 'Dashboard'
    }

    return render_template('home.html', **context)

@app.route('/ideas', methods=['GET', 'POST'])
def ideas():
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        author = request.form.get('author')
        category_id = request.form.get('category_id')

        idea = Idea(title, description, author, category_id).save()
        db.session.add(idea)
        db.session.commit()

        return redirect(url_for('show_idea', id=idea.id))

    context = {
        'title': 'Ideas',
        'ideas': Idea.query.all()
    }

    return render_template('ideas/index.html', **context)

@app.route('/ideas/<int:id>')
def show_idea(id):
    
    idea = Idea.query.filter_by(id=id).first()

    context = {
        'title': 'Viewing idea: {}'.format(idea.title),
        'idea': idea
    }

    return render_template('ideas/show.html', **context)

@app.route('/ideas/<int:id>', methods=['GET', 'POST'])
def update_idea(id):
    context = {
        'title': 'Ideas',
        'ideas': Idea.query.all()
    }

    return render_template('ideas/index.html', **context)

@app.route('/tags')
def tags():
    context = {
        'title': 'Tags',
        'tags': []
    }

    return render_template('tags.html', **context)

@app.route('/categories')
def categories():
    context = {
        'title': 'Categories',
        'categories': []
    }

    return render_template('categories.html', **context)


@app.route('/login',  methods=['GET', 'POST'])
def login():
    context = {
        'title': 'Login'
    }

    if request.method == 'POST':
        email = request.form.get('email')
        password = hash_password(request.form.get('password'))

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            flash('Welcome back, {}'.format(user.firstname), category='info')
            return redirect(url_for('home'))

        flash('No user was found that matched the credentials provided', category='danger')

    return render_template('auth/login.html', **context)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    context = {
        'title': 'Login'
    }

    if request.method == 'POST':
        
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        if password == password_confirmation:
            raise ValueError('Password submitted do not match')

        user = User(**{
            'firstname': request.form.get('firstname'),
            'lastname': request.form.get('lastname'),
            'username': request.form.get('username'),
            'password': hash_password(password),
            'email': request.form.get('email'),
        })

        db.session.add(user)
        db.session.commit()
        
        flash('User account has been registered. You should receive an eamil shortly', category='info')
        
        return redirect(url_for('home'))

    return render_template('auth/signup.html')

@app.route('/logout', methods=['POST'])
def logout():
    context = {
        'title': 'Sign up'
    }

    session.pop('user', None)
    flash('You have successfully logged out', category='success')
    
    return redirect(url_for('home'))

@app.route('/settings')
def settings():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=6060)
