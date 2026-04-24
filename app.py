from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__, static_folder='images', static_url_path='/images')

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year, lang='en')

if __name__ == '__main__':
    app.run(debug=True)
