from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home_func():
    return 'Welcome to homepage!'


@app.route('/about')
def about_func():
    # TODO
    # write some details about the website
    return redirect('/info')


@app.route('/info')
def info_func():
    return 'Welcome to info page!'


@app.route('/pay')
def pay_func():
    # TODO
    # write some details about the website
    return redirect(url_for('payment_func'))


@app.route('/payment')
def payment_func():
    return 'Welcome to payment page!'


if __name__ == '__main__':
    app.run()
