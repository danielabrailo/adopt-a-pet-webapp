from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from app import db
from app.posts.forms import PostForm
from app.models import Post
from flask_login import current_user, login_required
from app.users.utils import save_pet_picture

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(name=form.name.data, age=form.age.data, gender=form.gender.data, content=form.content.data,
                    user=current_user, adoption_info=form.adoption_info.data)
        if form.pictures.data:
            pet_pics = save_pet_picture(form.pictures.data)
            post.pictures = pet_pics
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.name, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.name = form.name.data
        post.age = form.age.data
        post.gender = form.gender.data
        post.content = form.content.data
        post.adoption_info = form.adoption_info.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.name.data = post.name
        form.age.data = post.age
        form.gender.data = post.gender
        form.content.data = post.content
        form.adoption_info.data = post.adoption_info
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.home'))
