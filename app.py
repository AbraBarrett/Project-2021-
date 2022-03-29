from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/mainpage')
def main_page():
   
    return render_template('mainpage.html')

@app.route('/vulnerabilities')
def contacts():
    return render_template('vulnerabilities.html')

@app.route('/antiviruses')
def new_things():
    return render_template('antiviruses.html')

if __name__ == '__main__':
    app.run()
