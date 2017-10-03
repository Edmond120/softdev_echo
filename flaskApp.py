from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    if("userName" in request.args):
        return render_template("greetings.html",name=request.args["userName"])
    else:
        return render_template("form.html")
if __name__ == '__main__':
        app.debug = True
        app.run()
