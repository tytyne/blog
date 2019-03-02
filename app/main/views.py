from flask import render_template,request,redirect,url_for
from . import main


from flask import render_template, request, redirect, url_for, abort
from ..models import User,Role,blog,Comment
from .forms import UpdateProfile, Createblogs, CommentForm
from .. import db
from flask_login import login_required, current_user
import markdown2



@main.route('/')
def index():
    business = blog.get_blogs('business')
    general = blog.get_blogs('general')

    title = 'blog'
    blog = blog.query.all()
    return render_template('index.html', title=title, blog=blog,business=business, general=general)


@main.route('/blogs/business')
def business():
    blogs = blog.get_blogs('business')

    return render_template('business.html', blogs=blogs)


@main.route('/blogs/general')
def general():
    blogs = blog.get_blogs('general')

    return render_template('general.html', blogs=blogs)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()


    return render_template('profile/update.html', form=form)


@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = blogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.text.data
        category = form.category.data

        new_blog = blog(blog_title=title, blog_content=blog,
                          category=category, user=current_user, likes=0, dislikes=0)
        new_blog.save_blog()
        return redirect(url_for('main.index'))

    title = 'New blog'
    return render_template('newblog.html', title=title, blog_form=form)



@main.route('/blog', methods=['GET', 'POST'])
def create_blogs():
    form = Createblogs()
    print(current_user.id)
    if form.validate_on_submit():


        # blog = form.blog.data


        # title = form.title.data
        blog = form.text.data
        category = form.category.data

        new_blog = blog(blog=blog, user_id=current_user.id,
                          category=category, likes=0, dislikes=0)
        new_blog.save_blog()
        return redirect(url_for('main.index'))

        title = 'New blog'
        return render_template('blog.html', form=form, user=current_user)




    #     new_blog = blog(blog=blog, user_id=current_user.id)

    #     db.session.add(new_blog)
    #     db.session.commit()

    #     return redirect(url_for('main.index'))

    # return render_template('blog.html', form=form, user=current_user)


@main.route('/blog/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def create_comments(id):
    form = CommentForm()
   
    if form.validate_on_submit():
        comment = form.text.data

    #     comment = form.comment.data

    #     new_comment = Comment(comment=comment, blog_id=id,user_id=current_user.id)
    #     db.session.add(new_comment)
    #     db.session.commit()

    # comment = Comment.query.filter_by(blog_id=id).all()

    # return render_template('comment.html', comment=comment, form=form)


        new_comment = Comment(comment = comment, user = current_user, blog_id = blog)

        new_comment.save_comment()

        comments = Comment.get_comments(blog)

    return render_template('blog.html', blog = blog, comment_form = form,comment = comment, date = posted_date)
