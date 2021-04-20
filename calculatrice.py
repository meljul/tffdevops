from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


def resultat():
    entry1 = request.form.get("entry1", type=int)
    entry2 = request.form.get("entry2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        resultat = entry1 + entry2
    else:
        resultat = 'Not a valid operation !'
    entry = resultat


if __name__ == '__main__':
    app.run(debug=True)