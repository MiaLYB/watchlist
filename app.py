import pip
from flask import Flask, render_template
name='Mia L'
movies=[
    {'title':'My Neighbor Toroto','year':'1988'},
    {'title':'Dead Poets Society','year':'1989'},
    {'title':'A Perfect World','year':'1993'},
    {'title':'Leon','year':'1994'},
    {'title':'Mahjong','year':'1996'},
    {'title':'Swallowtail','year':'1996'},
    {'title':'King of Comedy','year':'1999'},
    {'title':'Devils on the Doorstep','year':'1999'},
    {'title':'WALL-E','year':'2008'},
    {'title':'The Pork of Music','year':'2012'}
]
app=Flask(__name__)
#@app.route('/')
#@app.route('/index')
#@app.route('/home')
#@app.route('/user/<name>')

from flask import url_for
@app.route('/test')
def test_ur1_for():
    return 'test page'

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)
@app.route('/hello')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
@app.route('/user/<name>')
def user_page(name):
   return 'User:%s' % name
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

