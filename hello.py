# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    # URL을 통해 전달받은 name 값이 admin 인 경우 아래 로직을 탄다.
    # hello_admin 함수에 대한 URL 을 얻은 후, 그 값을 redirect 한다.
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    # URL을 통해 전달받은 name 값이 admin 이 아닌 경우 아래 로직을 탄다.
    # hello_guest 함수에 대한 URL 을 얻어내고, guest 변수에는 name 을 치환한 후 redirect 한다.
    else:
        return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.run()
