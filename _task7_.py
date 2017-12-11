from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('textbox.html')
@app.route('/endpoint',methods=['post'])
def endpoint():
    name=request.form['name']
    return '<h1> user input:'+name+'</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)
