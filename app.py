from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8f463f37daf12dc40a0b120d857a2644'

posts = [
    {
        'name': 'Kitty',
        'age': 3,
        'gender': 'Female',
        'date_posted': 'November 21, 2021'
    },
    {
        'name': 'Cat',
        'age': 5,
        'gender': 'Male',
        'date_posted': 'November 18, 2021'
    }
]


@app.route('/')
@app.route('/home')
def main():
    return render_template('home.html', posts=posts, title='Homepage')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('main'))
    return render_template('register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form, title='Login')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
