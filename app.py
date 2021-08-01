from flask import Flask, render_template
from operacao import resultado

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def bitcoin():
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run()