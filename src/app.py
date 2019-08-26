from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run(port=5000)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    response = make_response('<h1>Hello World!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/browser/useragent')
def browser():
    userAgent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(userAgent)

@app.route('/redirect')
def redirector():
    return redirect('http://www.google.com')

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

@app.route('/bootstrap_user/<name>')
def bootstrap_user(name):
    return render_template('bootstrap_user.html', name=name + 'teste')

@app.route('/user_inheritance/<name>')
def user_inheritance(name):
    return render_template('user_inheritance.html', name=name)