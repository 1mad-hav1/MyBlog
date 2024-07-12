from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy                                                                                      
from models import db, Post

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with db instance
db.init_app(app)


@app.route('/')                                     # for home page
def home():
    posts=Post.query.all()
    return render_template('home.html',posts=posts)

@app.route('/post/add', methods = ['GET','POST'])   # to add a post
def add_post():
    if request.method=='POST':
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        post=Post(title=title,content=content,author=author)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_post.html')

@app.route('/post/edit/<int:id>', methods = ['GET','POST'])
def edit_post(id):
    post=Post.query.get(id)
    if request.method=='POST':
        post.title=request.form['title']
        post.author=request.form['author']
        post.content=request.form['content']
        db.session.commit()
        return redirect(url_for('post_details',id=post.id))
    return render_template('edit_post.html',post=post)

@app.route('/post/<int:id>')
def post_details(id):
    post=Post.query.get(id)
    return render_template('post_details.html',post=post)

@app.route('/post/delete/<int:id>')
def delete_post(id):
    post=Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)