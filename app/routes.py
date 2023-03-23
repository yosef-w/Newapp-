from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
from app.models import Address

@app.route('/')
def index():
    return render_template('index.html', name='Yosef', logged_in=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('User confirmation form complete.')
        first = form.first_name.data
        last = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        print(first, last, phone, address)
        new_contact = Address(first_name = first, last_name = last, phone = phone, address = address)
        flash(f"Thank you {first} for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)