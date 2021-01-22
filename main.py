from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def uploadfile():
    f = request.files['file']
    if f.filename:
        # f.save(f.filename)
        return render_template('index.html', uploaded=True)
    else:
        return render_template('index.html', uploaded=False)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
