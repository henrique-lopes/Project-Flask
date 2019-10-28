from flask import Flask , render_template

app = Flask(__name__)

@app.route ('/index.html')
def index():

    return render_template("index.html")

@app.route ('/curso1.html')
def curso1():

    return render_template("curso1.html")

@app.route ('/curso2.html')
def curso2():

    return render_template("curso2.html")

@app.route ('/curso3.html')
def curso3():

    return render_template("curso3.html")

@app.route ('/curso4.html')
def curso4():

    return render_template("curso4.html")

@app.route ('/curso5.html')
def curso5():

    return render_template("curso5.html")

@app.route ('/estilo.css')
def estilo():

    return render_template("estilo.css")

app.run()