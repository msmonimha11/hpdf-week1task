from flask import Flask, render_template
app = Flask(__name__)

@app.route('/robots.txt')
def index():
    return render_template('error.html')
if __name__ == '__main__':
    app.run(debug=True)
