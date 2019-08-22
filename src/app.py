from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Hello World!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/conditional_user/<name>')
def conditional_user(name):
    return render_template('conditional_user.html', name=name)

@app.route('/users_list')
def users_list():
    names = ['raphael', 'castilho', 'costa']
    return render_template('users_list.html', names=names)

@app.route('/browser/useragent')
def browser():
    userAgent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(userAgent)

@app.route('/redirect')
def redirector():
    return redirect('http://www.google.com')