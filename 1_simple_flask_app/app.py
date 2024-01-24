from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'weblink.jpg', mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
