from flask import (Flask, send_file, url_for, jsonify, render_template)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    path = 'clean_data.csv'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
