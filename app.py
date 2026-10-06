
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():

    result = None

    if request.method == 'POST':
        principal = float(request.form['name'])
        rate = float(request.form['rate'])
        time = float(request.form['time'])

        result = (principal * rate * time) / 100
        total = principal + result
        return render_template('index.html', result=result, total=total , principal=principal, rate=rate, time=time)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, port=3500)

