from flask import Flask, render_template, redirect, url_for, flash
from wallet import firstuser
from forms import AccountForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Lord'

@app.route("/")
def hello_world():
    return "<p> hello_world </p>"

@app.route("/show_wallet")
def wallet_info1():
    message = firstuser()
    return render_template('wallet.html', message = message)

@app.route('/account', methods=['GET', 'POST'])
def account():
    form =AccountForm()
    if form.validate_on_submit():
        name = form.name.data
        initial_deposit = form.initial_deposit.data
        balance = form.balance.data

        # Add Logic to save data in the database

        flash(f'Account created for {name} with initial deposit {initial_deposit} and balance {balance}', 'success')
        return redirect(url_for('account'))
    return render_template('account.html', form=form)



