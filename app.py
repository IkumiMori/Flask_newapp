from flask import Flask
from flask import render_template,redirect,request,flash




app=Flask(__name__)
app.secret_key="manbearpig_MUDMAN888"


@app.route('/hello')
def index():
    flash("what's your name?")
    return render_template("index.html")


@app.route('/greet' , methods=['GET', 'POST'])
def greet():
    flash("HI " + str(request.form['name_input']) + ", great to see you")
    request.form['name_input']
    return render_template("index.html")
    



    


if __name__ == "__main__":
    app.run(debug=True) 