from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello_word():
    return render_template("index.html")
app.run(debug=True)
