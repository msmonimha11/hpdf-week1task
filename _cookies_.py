from flask import Flask,render_template,make_response,request
app = Flask(__name__)

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
    
    
if __name__ == '__main__':
    app.run(debug=True)
