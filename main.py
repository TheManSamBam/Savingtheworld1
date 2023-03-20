from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/linear')
def linear():
    return render_template('linear.html')

@app.route('/quadratic')
def quadratic():
    return render_template('quadratic.html')

@app.route('/cubic')
def cubic():
    return render_template('cubic.html')

@app.route('/easter_egg')
def easter():
    return render_template('easter.html')

@app.route('/graph', methods=["POST"])
def graph():
    eqn = request.form.get("eqn")
    x = np.linspace(-10,10,1000)
    fig1, axes = plt.subplots()
    axes.plot(x, eval(eqn))
    plt.xlim(-10,10)
    plt.ylim(-25,25)
    fig1.savefig('static/my_plot.png')
    return render_template('graph.html', a= eqn)
  
app.run(host='0.0.0.0', port=81, debug=True)
