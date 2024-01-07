from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder="Static")


@app.route('/')
def pgcentralmain():
    return render_template('Main.html')


if __name__ == '__main__':
    app.run()
