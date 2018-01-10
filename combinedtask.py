from __future__ import print_function
from flask import Flask,render_template,make_response,request
import requests,sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HelloWorld-Mahalakshmi'
@app.route('/authors',methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html',users=users)

@app.route('/setcookie')
def setcookie():
    resp=make_response('the cookie is set!')
    resp.set_cookie('name','mahalakshmi')
    resp.set_cookie('age','20')
    return resp
@app.route('/getcookies')
def getcookie():
    name=request.cookies.get('name')
    age=request.cookies.get('age')
    return render_template('display.html',name= name,age=age)
@app.route('/robots.txt')
def index():
    return render_template('error.html')
@app.route('/html')
def html():
    return render_template('layout.html')
@app.route('/input')
def box():
    return render_template('textbox.html')
@app.route('/endpoint',methods=['post'])
def endpoint():
        name = request.form['name']
        return '<h1> user input:'+name+'</h1>'
if __name__ == '__main__':
 app.run(debug=True)
                            
