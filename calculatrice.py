from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    entry1 = request.form.get("entry1", type=int)
    entry2 = request.form.get("entry2", type=int)

    if (entry1 == None or entry2 == None) :
        return render_template('form.html')

    result = entry1 + entry2

    return render_template('result.html',  htmlResult=result, htmlEntry1=entry1, htmlEntry2=entry2)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')