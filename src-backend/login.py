from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    print('Application is up and running!')
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug = True)
