from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


### Important note;
## store the index.html file which is to be rendered
## in a subfolder called template
