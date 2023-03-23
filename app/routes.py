from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html', name='Yosef', logged_in=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('User confirmation form complete.')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        print(first_name, last_name, phone, address)

        flash(f"Thank you {first_name} for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)